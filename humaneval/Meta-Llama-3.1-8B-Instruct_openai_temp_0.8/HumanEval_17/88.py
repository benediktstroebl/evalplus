### Musical Note Parser
#### Python Script

```markdown
from typing import List


def parse_music(music_string: str) -> List[int]:
    """
    Input to this function is a string representing musical notes in a special ASCII format.
    Your task is to parse this string and return list of integers corresponding to how many beats does each note last.

    Here is a legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quater note, lasts one beat

    :param music_string: String representing musical notes
    :return: List of integers corresponding to note durations
    """
    # Define a dictionary to map note types to their durations
    note_durations = {'o': 4, 'o|': 2, '.|': 1}

    # Split the input string into notes
    notes = music_string.split()

    # Use a list comprehension to parse each note and append its duration to the result list
    return [note_durations[note] for note in notes]


# Example usage:
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```

This script uses a dictionary to map note types to their durations. It then splits the input string into individual notes and uses a list comprehension to parse each note and append its duration to the result list. The example usage at the end demonstrates how to use the `parse_music` function to parse a string of musical notes.