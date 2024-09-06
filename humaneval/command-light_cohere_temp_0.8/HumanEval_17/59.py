Here is a self-contained Python function that solves the problem you described: 

```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string representing musical notes in a special ASCII format.
    'o whole note is four beats
    'o' - whole note
    'o|' - half note
    '|.' - quarter note
    Whole notes and half notes last until the next note with the same duration.

    quarter: last quarter note
    Parse the music into an array of beats.
 return: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]

# Test
test_music = """
o o| .| o| .| .| .| .| o o
o o| .| o| o| .| .| .| o o
o o o o o o o o| .|  o  o  o  o  o  o  o  o  o  o  o  o  o  o  o  o o o
"""
result = parse_music(test_music)
print(result)
```