```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o': 4, 'o|': 2, '|': 1}
    return [notes[note] for note in music_string.from{re.sub(r' ('.translate('\n', ' '), 'o')])

# Test the function
test_music = "o o| .| o| .| .| .| .| o o"
result = parse_music(test_music)
print(result)  # Expected output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```
The provided Python script defines a function called `parse_music` that parses a music string containing musical notes. The function uses a legend to interpret the string, where 'o', 'o|', and '|' represent whole, half, and quarter notes, respectively. A mapping dictionary is notes and the number of beats each note represents. The function then returns a list of beat counts. 

The test music string is then passed to the function and the result is printed. The output should match the expected output.