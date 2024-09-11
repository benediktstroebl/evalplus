```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Input to this function is a string representing musical notes in a special ASCII format.
    Your task is to parse this string and return list of integers corresponding to how many beats does each
    note lasts.

    :param music_string: A string representing musical notes in a special ASCII format.
    :return: A list of integers corresponding to how many beats does each note last.
    """
    note_lengths = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }
    
    # Split the input string into a list of notes
    notes = music_string.split()
    
    # Initialize an empty list to store the note lengths
    note_lengths_list = []
    
    # Iterate over each note in the list
    for note in notes:
        # Append the length of the current note to the list
        note_lengths_list.append(note_lengths[note])
    
    # Return the list of note lengths
    return note_lengths_list

# Test the function
print(parse_music('o o|.| o| o|.|..|..|..|. o o'))
```

This script defines a function `parse_music` that takes a string of musical notes as input, parses it, and returns a list of integers representing the length of each note. The function uses a dictionary to map each note character to its corresponding length. It then splits the input string into a list of notes, iterates over each note, and appends its length to a list. Finally, it returns the list of note lengths. The script includes a test case to demonstrate the function's usage.