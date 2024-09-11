```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    This function takes a string of musical notes in a special ASCII format and returns a list of integers
    representing the duration of each note in beats.

    The legend for the notes is as follows:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quarter note, lasts one beat

    :param music_string: A string of musical notes
    :return: A list of integers representing the duration of each note
    """

    # Create a dictionary to map the notes to their durations
    note_durations = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Split the input string into individual notes
    notes = music_string.split()

    # Initialize an empty list to store the durations
    durations = []

    # Iterate over each note
    i = 0
    while i < len(notes):
        # If the note is a whole note, it's just 'o'
        if notes[i] == 'o':
            durations.append(note_durations['o'])
        # If the note is a half note or a quarter note, it's 'o|' or '.|'
        elif notes[i] + '|' in note_durations:
            durations.append(note_durations[notes[i] + '|'])
            # Skip the '|' character
            i += 1
        i += 1

    return durations


# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```

However, the code above is not efficient when dealing with strings that contain 'o' followed by '|' because it checks all possible cases. Here is a more efficient code that handles this issue.


```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    This function takes a string of musical notes in a special ASCII format and returns a list of integers
    representing the duration of each note in beats.

    The legend for the notes is as follows:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quarter note, lasts one beat

    :param music_string: A string of musical notes
    :return: A list of integers representing the duration of each note
    """

    # Create a dictionary to map the notes to their durations
    note_durations = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Initialize an empty list to store the durations
    durations = []

    # Initialize an empty string to build the current note
    current_note = ''

    # Iterate over each character in the input string
    for char in music_string:
        # If the character is a space, the current note is finished
        if char =='':
            # If the current note is not empty, add its duration to the list
            if current_note:
                durations.append(note_durations[current_note])
                current_note = ''
        else:
            # Add the character to the current note
            current_note += char
            # If the current note is in the dictionary, add its duration to the list
            if current_note in note_durations:
                durations.append(note_durations[current_note])
                current_note = ''

    # If there's a note left over at the end, add its duration to the list
    if current_note:
        durations.append(note_durations