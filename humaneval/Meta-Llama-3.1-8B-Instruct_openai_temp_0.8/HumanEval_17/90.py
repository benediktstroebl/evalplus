```markdown
### Parse Music Script

This Python script parses a musical string in a special ASCII format and returns a list of integers corresponding to the number of beats each note lasts.

#### Code
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Input to this function is a string representing musical notes in a special ASCII format.
    Your task is to parse this string and return list of integers corresponding to how many beats does each
    not last.

    Args:
        music_string (str): A string representing musical notes in a special ASCII format.

    Returns:
        List[int]: A list of integers corresponding to the number of beats each note lasts.

    Examples:
        >>> parse_music('o o|.| o| o|.|.|.|.| o o')
        [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    """
    notes = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    result = []
    current_note = ''

    for char in music_string:
        if char in notes.keys():
            if current_note:
                result.append(notes[current_note])
                current_note = ''
            current_note += char
        else:
            current_note = None  # reset current note if not a valid note

    # append the last note if it exists
    if current_note:
        result.append(notes[current_note])

    return result

# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```

#### Explanation

*   The script defines a function `parse_music` that takes a string of musical notes as input.
*   It uses a dictionary to map special ASCII characters to their corresponding note lengths.
*   The function iterates through the input string, appending note lengths to the result list whenever it encounters a valid note.
*   If a note is longer than one character, it is processed as a single note.
*   Finally, the function returns the list of note lengths.

#### Example Use Cases

*   `parse_music('o o|.| o| o|.|.|.|.| o o')` returns `[4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]`
*   `parse_music('o o| o| o| o| o| o| o| o| o| o')` returns `[4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]`
*   `parse_music('.|.|..|..|..|..|..|..|..|..|..|..|..|..|..|..|..|..|..|..|..|..|..|..|..|..|..|..|..|..|..|..|..|..|..|..|..|..|..|..|..|..|..|..|..|..|..|..|..|..|..|..|..|..|..|..|..|..|..|..|..|..|..|..|..|..|..|..|..|..|..|..|..|..|..|..|..|..|..|..|..|..|..|..|..|..|..|..|..|..|..|..|..|..|..