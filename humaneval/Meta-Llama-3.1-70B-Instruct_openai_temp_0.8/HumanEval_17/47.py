```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """ Input to this function is a string representing musical notes in a special ASCII format.
    Your task is to parse this string and return list of integers corresponding to how many beats does each
    not last.

    Here is a legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quater note, lasts one beat
    """
    notes_legend = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Split the input string into individual notes
    notes = music_string.split()

    # Initialize an empty list to store the duration of each note
    note_durations = []

    # Initialize an empty string to build the current note
    current_note = ''

    # Iterate over each character in the input string
    for char in notes:
        # If the character is a space, skip it
        if char =='':
            continue

        # Add the character to the current note
        current_note += char

        # If the current note is in the legend, add its duration to the list and reset the current note
        if current_note in notes_legend:
            note_durations.append(notes_legend[current_note])
            current_note = ''

    return note_durations

# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```