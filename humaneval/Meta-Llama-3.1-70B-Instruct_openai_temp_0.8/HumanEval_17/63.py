```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    This function takes a string of musical notes in a special ASCII format, 
    parses the string, and returns a list of integers corresponding to the 
    number of beats each note lasts.

    Parameters:
    music_string (str): A string of musical notes in a special ASCII format.

    Returns:
    List[int]: A list of integers corresponding to the number of beats each note lasts.
    """

    # Define a dictionary to map notes to their corresponding beats
    notes_to_beats = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Split the input string into individual notes
    notes = music_string.split()

    # Initialize an empty list to store the beats
    beats = []

    # Initialize an empty string to build each note
    note = ''

    # Iterate over each character in the notes
    for char in notes:
        # If the character is a space, it means we've reached the end of a note
        if char == '':
            # If the note is not empty, add its beats to the list
            if note:
                beats.append(notes_to_beats[note])
                note = ''
        else:
            # If the character is not a space, add it to the current note
            note += char
            # If the note is in the dictionary, add its beats to the list
            if note in notes_to_beats:
                beats.append(notes_to_beats[note])
                note = ''

    # Return the list of beats
    return beats

# Example usage:
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```

However, the above solution doesn't split the notes correctly when two or more notes are adjacent without a space. We can modify the function to split the notes correctly by iterating over the input string and building each note manually.

Here's an updated version of the function:

```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    This function takes a string of musical notes in a special ASCII format, 
    parses the string, and returns a list of integers corresponding to the 
    number of beats each note lasts.

    Parameters:
    music_string (str): A string of musical notes in a special ASCII format.

    Returns:
    List[int]: A list of integers corresponding to the number of beats each note lasts.
    """

    # Define a dictionary to map notes to their corresponding beats
    notes_to_beats = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Initialize an empty list to store the beats
    beats = []

    # Initialize an empty string to build each note
    note = ''

    # Iterate over each character in the input string
    for char in music_string:
        # Add the character to the current note
        note += char
        # If the note is in the dictionary, add its beats to the list
        if note in notes_to_beats:
            beats.append(notes_to_beats[note])
            note = ''

    # Return the list of beats
    return beats

# Example usage:
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```