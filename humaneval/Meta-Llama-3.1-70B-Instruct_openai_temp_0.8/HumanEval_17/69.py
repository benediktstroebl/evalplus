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

    >>> parse_music('o o|.| o| o|.|.|.|.| o o')
    [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    """
    music_string = music_string.replace(' ', '')  # Remove spaces for easier parsing
    notes = {'o': 4, 'o|': 2, '.|': 1}  # Dictionary mapping notes to beats
    result = []  # List to store the result
    
    i = 0  # Index for parsing the string
    while i < len(music_string):
        if music_string[i:i+2] in notes:  # Check if the next two characters are a note
            result.append(notes[music_string[i:i+2]])  # Add the note to the result
            i += 2  # Move the index two positions forward
        else:
            result.append(notes[music_string[i]])  # Add the note to the result
            i += 1  # Move the index one position forward
    
    return result

# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```