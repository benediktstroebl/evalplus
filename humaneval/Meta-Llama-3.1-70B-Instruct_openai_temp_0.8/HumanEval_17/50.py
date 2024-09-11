```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    This function takes a string of musical notes in a special ASCII format and returns a list of integers.
    Each integer in the list corresponds to the number of beats a note lasts.

    :param music_string: A string representing musical notes.
    :return: A list of integers representing the duration of each note in beats.
    """
    
    # Define a dictionary to map each note to its duration
    note_durations = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }
    
    # Split the input string into individual notes
    notes = music_string.split()
    
    # Initialize an empty list to store the note durations
    durations = []
    
    # Initialize an empty string to build the current note
    current_note = ''
    
    # Iterate over each character in the input string
    for char in music_string:
        # If the character is a space, it marks the end of a note
        if char =='':
            # If the current note is not empty, add its duration to the list
            if current_note:
                durations.append(note_durations[current_note])
                current_note = ''
        else:
            # Add the character to the current note
            current_note += char
    
    # Add the duration of the last note to the list
    if current_note:
        durations.append(note_durations[current_note])
    
    return durations

# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))  # Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```