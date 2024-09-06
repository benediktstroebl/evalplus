```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = music_string.split(' ')
   
    notes
 # Remove leading and trailing white-spaces
    notes = [int(note.strip(note.strip()) for note in notes]
    return notes

# Example usage
test_parse_music = """
'o o| .| o| .| .| .| .| o o
"""

result = parse_music(test_parse_music)
print(result)  # Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```
This script defines a function `parse_music` that takes a music string as input and returns a list of integers. Each integer represents the medicines notes that are found in the string. The function splits the music string into individual notes and converts them into integers.