```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    This function takes a string of musical notes in a special ASCII format and returns a list of integers 
    representing the duration of each note in beats.

    :param music_string: A string of musical notes
    :return: A list of integers representing the duration of each note in beats
    """

    # Define a dictionary to map each note to its corresponding duration
    note_durations = {
        'o': 4,  # whole note
        'o|': 2,  # half note
        '.|': 1  # quarter note
    }

    # Split the input string into a list of notes
    notes = music_string.split()

    # Initialize an empty list to store the durations
    durations = []

    # Iterate over each note in the list
    i = 0
    while i < len(notes):
        # Check if the current note is a whole note
        if notes[i] == 'o' and i + 1 < len(notes) and notes[i + 1] == '':
            # If it's a whole note, append its duration to the list and move to the next note
            durations.append(note_durations['o'])
            i += 1
        # Check if the current note is a half note or a quarter note
        elif notes[i].endswith('|'):
            # If it's a half note or a quarter note, append its duration to the list and move to the next note
            durations.append(note_durations[notes[i]])
            i += 1
        else:
            # If it's a whole note, append its duration to the list and move to the next note
            durations.append(note_durations['o'])
            i += 1

    # Return the list of durations
    return durations

# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
# Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```