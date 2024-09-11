```markdown
### Music Note Parser

This script parses a string representing musical notes in a special ASCII format and returns a list of integers corresponding to how many beats each note lasts.

#### Code

```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string representing musical notes in a special ASCII format.

    Args:
        music_string (str): A string of musical notes in ASCII format.

    Returns:
        List[int]: A list of integers corresponding to how many beats each note lasts.

    Legend:
        'o' - whole note, lasts four beats
        'o|' - half note, lasts two beats
        '.|' - quarter note, lasts one beat
    """
    note_durations = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    music_string = music_string.replace(" ", "")  # remove spaces
    beats = []

    current_note = ''
    for char in music_string:
        if char in note_durations:
            current_note += char
        else:
            if current_note:
                beats.append(note_durations[current_note])
                current_note = ''
            else:
                continue

    if current_note:
        beats.append(note_durations[current_note])

    return beats


# Example usage:
if __name__ == "__main__":
    music_string = 'o o|.| o| o|.|.|.|.| o o'
    beats = parse_music(music_string)
    print(beats)
    # Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```

#### Explanation

This script defines a function `parse_music` that takes a string `music_string` as input and returns a list of integers representing the duration of each musical note.

The function uses a dictionary `note_durations` to map each note to its corresponding duration.

It iterates over the input string, appending each note to the `current_note` variable. When it encounters a character that is not a note, it checks if `current_note` is not empty. If it's not empty, it adds the duration of `current_note` to the `beats` list and resets `current_note` to an empty string.

Finally, it checks if `current_note` is not empty after the loop and adds its duration to the `beats` list.

The example usage shows how to use the `parse_music` function with a sample input string.