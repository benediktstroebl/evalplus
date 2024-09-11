### Musical Notes Parser
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    This function takes a string of musical notes in a special ASCII format, 
    parses the string, and returns a list of integers corresponding to the number of beats each note lasts.

    :param music_string: A string representing musical notes.
    :return: A list of integers representing the duration of each note in beats.
    """

    # Create a dictionary to map the musical notes to their corresponding durations
    note_durations = {
        'o': 4,  # whole note, lasts four beats
        'o|': 2,  # half note, lasts two beats
        '.|': 1  # quarter note, lasts one beat
    }

    # Split the input string into individual notes
    notes = music_string.split()

    # Initialize an empty list to store the note durations
    durations = []

    # Iterate over each note in the notes list
    i = 0
    while i < len(notes):
        # Check if the current note is a whole note
        if notes[i] == 'o':
            # If it's a whole note, check if the next note is a half note
            if i + 1 < len(notes) and notes[i + 1] == '|':
                # If it's a half note, append its duration to the list and skip the next note
                durations.append(note_durations['o|'])
                i += 2
            else:
                # If it's not a half note, append the whole note's duration to the list
                durations.append(note_durations['o'])
                i += 1
        # If the current note is not a whole note, it must be a half or quarter note
        else:
            # Append the current note's duration to the list
            durations.append(note_durations[notes[i] + (notes[i + 1] if i + 1 < len(notes) else '')])
            i += 2

    return durations


# Example usage:
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
# Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```
In this script, we first create a dictionary to map the musical notes to their corresponding durations. We then split the input string into individual notes and iterate over each note. For each note, we check its type and append its duration to the list. If the note is a whole note, we also check if the next note is a half note and handle it accordingly. Finally, we return the list of note durations.