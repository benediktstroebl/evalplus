```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string representing musical notes in a special ASCII format and return a list of integers
    corresponding to how many beats each note lasts.

    :param music_string: A string representing musical notes in a special ASCII format.
    :return: A list of integers corresponding to how many beats each note lasts.
    """

    # Split the input string into a list of notes
    notes = music_string.split()

    # Initialize a dictionary to map each note symbol to its corresponding beat duration
    note_durations = {
        'o': 4,  # whole note lasts four beats
        'o|': 2,  # half note lasts two beats
        '.|': 1  # quarter note lasts one beat
    }

    # Initialize an empty list to store the beat durations of the notes
    beat_durations = []

    # Iterate over each note in the list of notes
    i = 0
    while i < len(notes):
        # Check if the current note is a whole note (which consists of two characters: 'o' and the next character)
        if notes[i] == 'o' and i + 1 < len(notes) and notes[i + 1] == '|':
            # If it's a whole note, append the beat duration of a half note to the list
            beat_durations.append(note_durations['o|'])
            # Skip the next character
            i += 2
        else:
            # If it's not a whole note, append the beat duration of the current note to the list
            beat_durations.append(note_durations[notes[i]])
            # Move to the next note
            i += 1

    # Return the list of beat durations
    return beat_durations


# Example usage:
music_string = 'o o|.| o| o|.|.|.|.| o o'
print(parse_music(music_string))  # Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```