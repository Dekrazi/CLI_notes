import json
from colorama import Fore, Style, init

init(autoreset=True)

file_path = 'notes.json'

def load_notes(file_path):
    try:
        with open(file_path, 'r') as file:
            loaded_notes = json.load(file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        loaded_notes = []
    return loaded_notes

def save_notes(notes, file_path):
    with open(file_path, 'w') as file:
        json.dump(notes, file, indent=2)

notes = load_notes(file_path)

def print_colored(text, color=Fore.WHITE, style=Style.NORMAL):
    print(style + color + text + Style.RESET_ALL)

def menu():
    print_colored("Menu:")
    for k, v in menu_options.items():
        print_colored(f"{k}: {v}", Fore.CYAN)

def add_note():
    note_title = input("Note title: ")
    note_body = input("Note body: ")
    notes.append({"title": note_title, "body": note_body})
    save_notes(notes, file_path)
    print_colored("Note has been added successfully!", Fore.GREEN)

def show_all_notes():
    print_colored("\n----- NOTES -----", Fore.MAGENTA)
    for index, note in enumerate(notes):
        print_colored(f"{index + 1}: {note['title']} - {note['body']}", Fore.YELLOW)
    print_colored("-----------------", Fore.MAGENTA)

def edit_note():
    show_all_notes()
    choose_index = int(input("Choose note index to edit: "))
    if 1 <= choose_index <= len(notes):
        new_note_title = input("New note title: ")
        new_note_body = input("New note body: ")
        notes[choose_index - 1] = {"title": new_note_title, "body": new_note_body}
        save_notes(notes, file_path)
        print_colored("Note has been updated successfully!", Fore.GREEN)
    else:
        print_colored("Wrong index.", Fore.RED)

def delete_note():
    show_all_notes()
    choose_index = int(input("Choose note index to delete: "))
    if 1 <= choose_index <= len(notes):
        notes.pop(choose_index - 1)
        save_notes(notes, file_path)
        print_colored("Note has been deleted successfully!", Fore.GREEN)
    else:
        print_colored("Wrong index.", Fore.RED)

menu_options = {
    1: "Add",
    2: "Show all",
    3: "Edit",
    4: "Delete",
    5: "Save and Quit",
    6: "Quit"
}

while True:
    menu()

    choice = input("How do you want to proceed? ")

    if choice == "1":
        add_note()
    elif choice == "2":
        show_all_notes()
    elif choice == "3":
        edit_note()
    elif choice == "4":
        delete_note()
    elif choice == "5":
        print_colored("Notes have been saved. You have closed the program.", Fore.BLUE)
        break
    elif choice == "6":
        print_colored("You have closed the program without saving.", Fore.BLUE)
        break
    else:
        print_colored("-----------------", Fore.RED)
        print_colored("Invalid input.", Fore.RED)
        print_colored("-----------------", Fore.RED)
