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
    music_dict = {'o': 4, 'o|': 2, '.|': 1}  # Dictionary to map note to beats
    notes = music_string.split()  # Split the input string into individual notes
    beats = [music_dict[note] for note in notes]  # Use list comprehension to get the beats for each note
    return beats  # Return the list of beats


# Example usage
print(parse_music('o o|.| o| o|.|.|.|.| o o'))  # Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```

In this code, we first define a dictionary `music_dict` that maps each note to the number of beats it lasts. We then split the input string into individual notes using the `split()` method. Next, we use list comprehension to create a new list `beats` where each element is the number of beats for the corresponding note. Finally, we return the `beats` list.