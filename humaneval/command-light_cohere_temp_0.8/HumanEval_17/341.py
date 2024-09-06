```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o': 4, 'o|': 2, '.|': 1}
    beats = [notes[note] for note in music_string.split(' '|')]
    return [beats[i] for i, beat in enumerate(beats)]

# Test the function with an input string
test_music = """o o| .| o| .| .| .| o o"""
actual = parse_music(test_music)
print("Actual:", actual)

# Reference values
expected = [4, 2, 1, 2, 1, 1, 1, 4]
print("Expected:", expected)
``` 
This code defines a function **`parse_music`** that takes a music string in a special ASCII format representing musical notes. The function then uses a predefined dictionary to map notes to the corresponding number of beats they last. It splits the string by '|' character and returns the number of beats corresponding to each note. The test code demonstrates that the function with a test string and compares the actual result with the expected result.