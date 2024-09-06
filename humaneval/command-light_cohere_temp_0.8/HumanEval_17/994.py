Here's a self-contained Python script that includes a function named `parse_music`, which is designed to convert a given music string into a list of integers representing the number of beats for each note.

```python
import typing


def parse_music(music_string: str) -> List[int]:
    """
    Input to this function is a string representing musical notes in a special ASCII format.
    The task is to parse this string and return a list of integers corresponding to how many beats does each note last.

    Here is the legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quarter note, lasts one beat

    :return: A list of integers, where each integer represents the number of beats for a specific note.
    """
    legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quarter note, lasts one beat

    return [int(note) for note in music_string.ep legend:
    }
```

You can use this function to solve the given markdown code block's problem.