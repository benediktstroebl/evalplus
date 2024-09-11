```markdown
### Musical Note Parser

#### Problem Description
Parse a string of musical notes in ASCII format and return a list of integers representing the number of beats each note lasts.

#### ASCII Legend
- 'o' - whole note, lasts four beats
- 'o|' - half note, lasts two beats
- '.|' - quarter note, lasts one beat

#### Code Solution
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string of musical notes in ASCII format and return a list of integers representing the number of beats each note lasts.

    Args:
    music_string (str): A string representing musical notes in a special ASCII format.

    Returns:
    List[int]: A list of integers corresponding to how many beats each note lasts.
    """
    # Define a dictionary to map musical notes to their corresponding beat counts
    note_beat_counts = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Split the input string into individual notes
    notes = music_string.split()

    # Use a list comprehension to create a list of beat counts for each note
    beat_counts = [note_beat_counts[note] for note in notes]

    return beat_counts

# Example usage
print(parse_music('o o|.| o| o|.|.|.|.| o o'))
```
#### Explanation
This script uses a dictionary to map musical notes to their corresponding beat counts. It then splits the input string into individual notes, using a list comprehension to create a list of beat counts for each note. The resulting list is returned by the function.

The example usage demonstrates how to call the `parse_music` function with a sample input string and print the resulting list of beat counts.