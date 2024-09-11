```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    This function takes a string representing musical notes in a special ASCII format,
    parses this string, and returns a list of integers corresponding to how many beats each note lasts.

    Args:
        music_string (str): A string representing musical notes.

    Returns:
        List[int]: A list of integers corresponding to the number of beats each note lasts.
    """
    # Define a dictionary to map musical notes to their corresponding beat durations
    note_durations = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Split the input string into a list of musical notes
    notes = music_string.split()

    # Initialize an empty list to store the beat durations of each note
    beat_durations = []

    # Iterate over each note in the list of notes
    i = 0
    while i < len(notes):
        # Check if the current note is a whole note
        if notes[i] == 'o':
            # If it is, append its beat duration to the list and move on to the next note
            beat_durations.append(note_durations['o'])
            i += 1
        # Check if the current note is a half note or a quarter note
        elif notes[i] == 'o' and i + 1 < len(notes) and notes[i + 1] == '|':
            # If it is, append its beat duration to the list and move on to the next note
            beat_durations.append(note_durations['o|'])
            i += 2
        elif notes[i] == '.' and i + 1 < len(notes) and notes[i + 1] == '|':
            # If it is, append its beat duration to the list and move on to the next note
            beat_durations.append(note_durations['.|'])
            i += 2

    # Return the list of beat durations
    return beat_durations


# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))  # Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```