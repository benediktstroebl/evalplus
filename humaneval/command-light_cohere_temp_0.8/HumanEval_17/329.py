```python
from typing import List
def parse_music(music_string: str) -> List[int]:
    """
    This function takes in a string representing musical notes in a special ASCII format.
    Here's legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quarter note, lasts one beat

    Returns a list of integers corresponding to how many beats each note lasts.
    """
   
    legend below is a quick reference:
    ```
    [o, 2, 1, 2, 1, 1, 1, 1, 4, 4]

Here's how the above function would be used:
```python
# Test string input
music_string = "o o| .| o| .| .| .| .| o o"

# Function call
note_list = parse_music(music_string)

print(note_list)
```