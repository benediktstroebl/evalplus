### Music Parser Script
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string representing musical notes and return a list of integers
    corresponding to the duration of each note.

    Args:
    music_string (str): A string representing musical notes in a special ASCII format.

    Returns:
    List[int]: A list of integers representing the duration of each note.
    """

    # Define a dictionary to map note characters to their durations
    note_durations = {
        'o': 4,
        'o|': 2,
        '|': 1  # Updated to '<|' for consistency, further changed to '.' for quater note
        # Removed 'o' for '<' because whole notes are already defined, and 'o|' for '.' because half note is also defined
    }

    # Initialize an empty list to store the durations of each note
    note_durations_list = []

    # Iterate over each character in the music string
    for i, char in enumerate(music_string):
        # If we've encountered a '|' and it's not at the end of the string
        if char == '|' and i < len(music_string) - 1:
            # If the next character is 'o' then we have a whole note
            if music_string[i + 1] == 'o':
                note_durations_list.append(note_durations['o'])
            # If the next character is '.' then we have a half note
            elif music_string[i + 1] == '.':
                note_durations_list.append(note_durations['o|'])
            # If the next character is '.' then we have a quarter note
            elif music_string[i + 1] == '.':
                note_durations_list.append(note_durations['|'])
        # If we've encountered a 'o' or '.' then it's a whole or a quarter note respectively
        elif char == 'o':
            note_durations_list.append(note_durations['o'])
        elif char == '.':
            note_durations_list.append(note_durations['|'])

    return note_durations_list

# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```