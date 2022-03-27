"""
Notebook implementation module
"""
import datetime
import sys
from tabnanny import check

from idna import check_bidi
# the id available for the next note  
available_id = 0

class Note(object):
    '''Represent a note in the notebook.
    Match against a string in searches.
    Store tags for each note.
    '''
    def __init__(self, note_text, note_tags=''):
        '''Initialize a note with a note_text and optional note_tags.
        Automatically assign an id and creation date.
        '''
        global available_id
        self.note_text = note_text
        self.note_tags = note_tags
        self.note_id = available_id
        available_id += 1
        self.creation_date = datetime.date.today()
        return
    
    def contains(self, search_string):
        '''Determines if the note contains the search_string.
        Check both the note_text and note_tags for the presence 
        of the search_string as a sub string in the note.
        The search is case-sensitive.
        '''
        return search_string in self.note_text or search_string in self.note_tags
    
    def __str__(self):
        '''String representation of the object
        '''
        return('Note Id = {0}, Date = {1}, Text = {2}, Tags = {3}'
              .format(self.note_id, self.creation_date, self.note_text, self.note_tags)) 



class Notebook(object):
    '''
    A collection that allows user to:
    1. Create a new note
    2. Modify the text of an existing note
    3. Tag a note
    4. Search inside the note text and tags
    '''    

    def __init__(self):
        '''
        Initialize a notebook with an empty list of notes
        '''
        self.notes_list = []
        
    def add_new_note(self, note_text, note_tags=''):
        '''
        Create a new note and add to notebook.
        '''
        self.notes_list.append(Note(note_text, note_tags))
        
    def find_note_by_id(self, note_id):
        '''
        Returns the note with id that matches given one.  
        Currently performs an inefficient linear scan.
        '''
        for note in self.notes_list:
            if note.note_id == note_id:
                return note
        return None

    def get_number_of_notes(self):
        '''Return the number of notes
        '''
        return len(self.notes_list)
    
    def get_text(self, note_id):
        '''Find note with the given id and 
        return its text
        '''
        note = self.find_note_by_id(note_id)  
        return note.note_text

    def get_tags(self, note_id):
        '''Find note with the given id and 
        return its text
        '''
        note = self.find_note_by_id(note_id)  
        return note.note_tags
    
    def replace_note_text(self, note_id, note_text):
        '''Find note with the given id and replace
        its text with the given text
        '''
        note = self.find_note_by_id(note_id)  
        note.note_text = note_text
    
    def replace_note_tags(self, note_id, note_tags):
        '''Find note with the given id and replace
        its tags with the given tags
        '''
        note = self.find_note_by_id(note_id)  
        note.note_tags = note_tags
    
    def search_notes(self, search_string):
        '''Find all the notes that contain the search string
        '''
        return [note for note in self.notes_list if note.contains(search_string)]
    
    def __str__(self):
        """
        Represent notebook when printing
        """
        result = ''
        for note in self.notes_list:
            result += str(note)
            result += '\n'
        return result



class Menu:
    '''Display a menu and respond to choices when run.'''

    def __init__(self):
        self.notebook = Notebook()
        self.choices = {
            '1': self.display_notes,
            '2': self.search_notes,
            '3': self.add_new_note,
            '4': self.modify_note,
            '5': self.quit
        }

    def display_menu(self):
        '''Displays the menu to the user.
        Returns the choice as string.
        '''
        print('''
        Notebook Menu
        
        1. Display Notes
        2. Search Notes
        3. Add Note
        4. Modify Note
        5. Quit
        ''')
    

    def run(self):
        '''Display the menu and respond to choices.'''
        while True:
            self.display_menu()
            choice = input("Enter an option: ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print(f"{choice} is not a valid choice")

    def display_notes(self):
        '''Displays the notes to the user. 
        '''
        for note in self.notebook.notes_list:
            print('\n\t{0}'.format(note))
        
    def search_notes(self):
        '''Asks the user for a search pattern.
        Displays any matching note found.
        '''
        search_string = input('\n\tEnter the string to search for: ')
        matching_notes = self.notebook.search_notes(search_string)
        print('\tThere are {0} notes matching the string "{1}":'.format(len(matching_notes), search_string))
        for note in matching_notes:
            print('\n\t{0}'.format(note))
        
    def add_new_note(self):
        '''Modifies the text and tags for a note.
        '''
        note_text = input('\n\tEnter the text for the note: ')
        note_tags = input('\tEnter tags for the note: ')
        self.notebook.add_new_note(note_text, note_tags)
        print('\tNote has been added')

    def check_id_validity(self, note_id):
        if isinstance(note_id, int):
            return note_id < self.notebook.get_number_of_notes()
        return False
        
    def modify_note(self):
        '''Modifies the text and tags for a note.
        '''
        note_id = input('\n\tEnter a note id: ')
        if self.check_id_validity(note_id):
            note_id = int(note_id)
            note_text = input('\n\tEnter the text for the note: ')
            note_tags = input('\tEnter tags for the note: ')
            if note_text:
                self.notebook.replace_note_text(note_id, note_text)
            if note_tags:
                self.notebook.replace_note_tags(note_id, note_tags)
        else:
            print('\tThere are no notes with the id "{0}".'.format(note_id))

    def quit(self):
        print("Thank you for using the notebook.")
        sys.exit(0)


if __name__ == "__main__":
    Menu().run()