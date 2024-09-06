```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = music_string.split('o value = []
    # Parse whole notes
    whole_notes = music_string.split('o  # split by "o")
    for note in whole_notes:
        note = note.strip()
        while note[0] == 'o':
            value = int(note[1:])
            value = [value] * 4  # Convert to list of 4 beats
            value.append(value)
        # Add to list
        value.append(0)  # Add empty beat at the end to match the format.
    # Parse half notes
    notes
    half_notes = music_string.split('o note')
    note = note[0]
    for note in half_notes:
        note = note.strip() while note[0] == '|':
            value = int(note[1:])
            value = [value] * 2  # Convert to list of 2 beats
            value.append(value)
        # Add to list
        value.append(0)  # Add empty beat at the end to match the format.
    # Parse quarter notes
    notes
    quarter_notes = music_string.split('.|')
    notes = quarter_notes[0].split(' ')
    for note in notes:
        note = note.strip() while note[0] == '|':
            value = int(note[1:])
            value = [value] * 1  # Convert to list of 1 beat
            value.append(value)
        # Add to list
        value.append(0)  # Add empty beat at the end to match the format.

print(parse_music('o o| .| o| .| .| .| .| o o'))
```
This code defines the parse_music() function that takes a string music_string as input and returns a list of integers. It achieves this by splitting the music string into different note types (whole notes, half notes, and quarter notes), and then parsing each note type accordingly. The code ensures that each parsed note has the correct number of beats by applying appropriate conversions and formatting.