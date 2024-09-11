```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    This function parses a string of musical notes in a special ASCII format and returns a list of integers 
    representing the duration of each note in beats.

    :param music_string: A string of musical notes
    :return: A list of integers representing the duration of each note
    """

    # Define a dictionary to map each note to its duration
    note_to_duration = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Split the input string into individual notes
    notes = music_string.split()

    # Initialize an empty list to store the duration of each note
    durations = []

    # Initialize an empty string to build each note
    note = ''

    # Iterate over each character in the string
    for char in notes:
        # If the character is a space, it means we've reached the end of a note
        if char == 'o':
            # If the note is not empty, it means we've already processed a note
            if note:
                # Add the duration of the note to the list of durations
                durations.append(note_to_duration[note])
                # Reset the note
                note = ''
            # Add the character to the note
            note = char
        else:
            # Add the character to the note
            note += char
            # Add the duration of the note to the list of durations
            durations.append(note_to_duration[note])
            # Reset the note
            note = ''

    # If there's a note left over at the end, add its duration to the list
    if note:
        durations.append(note_to_duration[note])

    return durations

# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```

In this code:

*   We define a dictionary `note_to_duration` that maps each note to its duration.
*   We split the input string into individual notes.
*   We iterate over each character in the string, building each note and adding its duration to the list of durations.
*   Finally, we return the list of durations.

This code will correctly parse the input string and return the list of durations.