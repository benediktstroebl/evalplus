```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4, 'o|': 2, '|': 1,
        '.' : 1,
    }
    return [notes[char] for char in music_string.

# Test cases
test_music_str = 'o o| .| o| .| .| .| .| o o'
test_music_str2 = '.'

result1 = parse_music(test_music_str)
result2 = parse_music(test_music_str2)

print(f"Test 1 - Parsed notes:", result1)
print("Test 2 - Parsed notes:", result2)
``` 
This code defines a function **parse_music** that takes a music string as input and parses it into a list of integers representing the number of beats for each note. The function uses a legend to map the music characters to their respective beat values. The output of the code will display the parsed results for the two test cases.