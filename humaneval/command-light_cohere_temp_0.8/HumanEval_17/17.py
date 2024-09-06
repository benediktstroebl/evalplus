```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = music_string.split(' ') ')
    whole_notes = [int(x) for x in music_string.split('o all] in [1, 4, 8, 16]
    half_notes = [int(x) for x in music_string.split('|')] in [1, 2, 4]
    quarter_notes = [int(x) for x in music_string.split('.')] in [1]

    return [whole_notes, half_notes, quarter_notes]

# Test the function
test_string = "o o| .| o| .| .| .| o o"
expected = [4, 2, 1, 2, 1, 1, 1, 1, 4]
result = parse_music(test_string)
assert result == expected, "Error: Expected %s, got %s" % (expected, result)
```
This code defines a function **`parse_music`** that parses music notes, and its output is a list of integers corresponding to the duration of each note. The function handles the multiple note lengths and formats, such as whole notes, half notes, and quarter notes. It splits the music string by ' ' and '|', and then converts these to integers to meet the specified requirements. The test string **`test_string`** is passed to the **`parse_music`** function to verify the correctness of the parsing.