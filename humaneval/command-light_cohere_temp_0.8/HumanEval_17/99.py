```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4, 'o|': 2, '|': 1
    }
    return [notes[note] for note in music_string.test_music_parse(music_string)]

# Example test cases
test_music_parse = []
test_music_parse.add_str("""o o| .| o| .| .| .| .| .| o o")
test_music_parse.add_str("""")
test_music_parse.add_str("""o|")
test_music_parse.add_str("""o o o| .| o| .| .| .| o o")
test_music_parse.add_str("'| ")
test_music_parse.add_str(""" o o| o| o| .| .| o o o")

print(test_music_parse)
``` 
This script defines a function called `parse_music` that takes a music string in a format similar to the legend provided. The function maps the notes to their respective durations (whole, half, or quarter notes) and returns a list of corresponding beat counts. The test cases demonstrate the following:
- Two whole notes, each lasting four beats.
- A half note lasting two beats.
- A quarter note lasting one beat.
- Two half notes, each lasting two beats.
- A quarter note and a whole note, each lasting one beat.
- Two whole notes, each lasting four beats.
- An invalid string (missing a note).

The script also adds a set of test cases to ensure that the `parse_music` function is working correctly.