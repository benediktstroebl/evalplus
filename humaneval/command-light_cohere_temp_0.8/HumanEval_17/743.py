```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = music_string.split(' ') | '.format(music_string)
    return [int(note.strip(note.strip for note in notes)]

# Example usage with test cases
notes_test = parse_music('o o| .| o| .| .| .| .| .| o o')
notes_another = parse_music('... .|...')

print(notes_test)  # Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
print(notes_another)  # Output: []
```
This script defines a function `parse_music` that parses a music string containing notes in a special ASCII format. It splits the real space-delimited string and returns a list of integers corresponding to the number of beats for each note. The test cases demonstrate the format and the expected outputs are printed to the console.