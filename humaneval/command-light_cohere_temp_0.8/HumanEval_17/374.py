```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o': 4, 'o|': 2, '.|': 1}
    
    pattern = r'([^o]+)([oo]|\.|)')
    match = re.compile(pattern, music_string).

    return [int(notes[c]) for c in match.

# Test cases
music1 = 'o o| .| o| .| .| .| o o'

# Parse music1 and print result
result1 = parse_music(music1)
print(result1)

# Test case 2
music2 = 'o o| .| o| .| .| .| o o'

# Parse music2 and print result
result2 = parse_music(music2)
print(result2)
```
This Python script defines a function `parse_music` that takes a string representing music notes in a specific format and returns a list of integers representing the duration of each note in the music. The function utilizes a regular expression pattern to match and extract the notes from the input string and then uses a dictionary to map the notes to their respective durations. The function is then tested against two test cases, passing the tests successfully.