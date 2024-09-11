```python
from typing import List


def parse_music(music_string: str) -> List[int]:
    """
    This function parses a given string representing musical notes in a special ASCII format.
    It returns a list of integers corresponding to how many beats each note lasts.

    The legend for the music string is:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quarter note, lasts one beat
    """
    notes_beats = {
        'o': 4,  # whole note
        'o|': 2,  # half note
        '.|': 1  # quarter note
    }

    music_list = music_string.split()  # split the string into a list of notes
    beats_list = [notes_beats[note] for note in music_list]  # get the beats for each note
    return beats_list


# Test the function
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```

In this script, we define a dictionary `notes_beats` that maps each note to its corresponding number of beats. We then split the input string into a list of notes and use a list comprehension to create a new list where each note is replaced with its corresponding number of beats. Finally, we return this list of beats.