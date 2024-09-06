```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    This function is designed to parse a string representing musical notes in a special format.
    - It task is to identify the number of beats each note will take, 
    and return this information as a list of integers.
	Format:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quarter note, lasts one beat

    Args:
    music_string (str): The input string is a sequence of musical notes in the specified format.
    Returns: A list of integers, where each integer represents the number of beats a corresponding note lasted.

Test cases are included to verify the correctness of the function. 
```