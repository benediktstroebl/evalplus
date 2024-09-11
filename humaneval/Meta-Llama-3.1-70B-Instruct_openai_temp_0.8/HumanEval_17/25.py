```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    This function takes a string of musical notes in a special ASCII format and returns a list of integers
    representing the number of beats for each note.

    The legend for the ASCII format is:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quater note, lasts one beat

    :param music_string: A string representing musical notes in a special ASCII format.
    :return: A list of integers corresponding to how many beats each note lasts.
    """

    # Define a dictionary to map each note to its corresponding beat duration
    note_beats = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Split the input string into individual notes
    notes = music_string.split()

    # Initialize an empty list to store the beat durations of the notes
    beat_durations = []

    # Iterate over each note in the notes list
    i = 0
    while i < len(notes):
        # Check if the current note is a whole note
        if notes[i] == 'o':
            # If the next note is not '|' then it's a whole note
            if i == len(notes) - 1 or notes[i + 1]!= '|':
                beat_durations.append(note_beats['o'])
            # If the next note is '|' then it's a half note
            else:
                beat_durations.append(note_beats['o|'])
                i += 1
        # If the current note is not a whole note, it's either a half note or a quarter note
        elif i < len(notes) - 1 and notes[i + 1] == '|':
            # Get the note by combining the current and next note
            note = notes[i] + notes[i + 1]
            # Append the beat duration of the note to the beat_durations list
            beat_durations.append(note_beats[note])
            # Increment the index by 2 to skip the '|' character
            i += 1
        i += 1

    return beat_durations

print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```