```python
from typing import List


def parse_music(music_string: str) -> List[int]:
    """
    Input to this function is a string representing musical notes in a special ASCII format.
    Your task is to parse this string and return list of integers corresponding to how many beats does each
    not last.

    Here is a legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quater note, lasts one beat

    Args:
    music_string (str): A string representing musical notes in a special ASCII format.

    Returns:
    List[int]: A list of integers corresponding to how many beats does each note last.
    """
    notes = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }
    beats = []
    current_note = ''
    for char in music_string:
        if char in notes:
            if current_note:
                beats.append(notes[current_note])
                current_note = ''
            current_note += char
        elif char =='':
            if current_note:
                beats.append(notes[current_note])
                current_note = ''
        else:
            raise ValueError(f"Invalid note character: {char}")
    if current_note:
        beats.append(notes[current_note])
    return beats


# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
# Expected output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```
This script uses a dictionary to map note characters to their corresponding beat lengths, then iterates through the input string, adding the beat length of each note to a list. If it encounters any invalid note characters, it raises a ValueError. Finally, it returns the list of beat lengths.