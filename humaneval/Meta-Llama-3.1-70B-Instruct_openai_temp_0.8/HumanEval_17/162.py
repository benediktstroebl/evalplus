```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string representing musical notes in a special ASCII format and return a list of integers 
    corresponding to how many beats each note lasts.

    :param music_string: A string representing musical notes
    :return: A list of integers corresponding to the number of beats each note lasts
    """
    # Define a dictionary to map note symbols to their corresponding beats
    note_beats = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Split the input string into a list of notes
    notes = music_string.split()

    # Initialize an empty list to store the beats of each note
    beats = []

    # Iterate over each note
    i = 0
    while i < len(notes):
        # Check if the note is a whole note
        if notes[i] == 'o':
            # If it is, check the next note
            if i + 1 < len(notes) and notes[i + 1] == '|':
                # If the next note is '|', it's a half note
                beats.append(note_beats['o|'])
                i += 2
            else:
                # Otherwise, it's a whole note
                beats.append(note_beats['o'])
                i += 1
        # If the note is not a whole note, it must be a half note or a quarter note
        else:
            # Check the next note
            if i + 1 < len(notes) and notes[i + 1] == '|':
                # If the next note is '|', it's a half note or a quarter note
                if notes[i] == '.':
                    # If the current note is '.', it's a quarter note
                    beats.append(note_beats['.|'])
                    i += 2
                else:
                    # Otherwise, it's a half note
                    beats.append(note_beats['o|'])
                    i += 2
            else:
                # If the next note is not '|', it's a whole note or a half note without the '|' symbol
                # In this case, we assume it's a whole note
                beats.append(note_beats['o'])
                i += 1

    return beats


# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```

However, the given test case does not provide enough information about the input string and it seems that the task description is missing some information about how notes are separated in the string. Based on the example test case, we can rewrite the `parse_music` function in a more concise way:

```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string representing musical notes in a special ASCII format and return a list of integers 
    corresponding to how many beats each note lasts.

    :param music_string: A string representing musical notes
    :return: A list of integers corresponding to the number of beats each note lasts
    """
    # Define a dictionary to map note symbols to their corresponding beats
    note_beats = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Split the input string into a list of notes
    notes = music_string.split()

    # Initialize an empty list to store the beats of each note
    beats = []

    # Iterate over each note
    i = 0
    while i < len(notes):
        # Check if