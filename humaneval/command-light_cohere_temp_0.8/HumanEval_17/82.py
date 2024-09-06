```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o': 4, 'o|': 2, '|': 1}
    notes_in_music = music_string.split(' ') | [']'
    
    return [notes[note[0]] for note in notes_in_music]

# Test cases
def test_parse_music():
    music_str = 'o o| .| o| .| .| .| .| o o'
    expected = [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    
    actual = parse_music(music_str)
    assert actual == expected

if __name__ == "__main__":
    test_parse_music()
```
This Python code defines a function `parse_music` that parses a given music string representing musical notes in a special ASCII format and returns a list of integers indicating the number of beats for each note. The function uses a legend where 'o' stands for a whole note lasting four beats, 'o|' represents a half note lasting two beats, and '|' stands for a quarter note lasting one beat. 

The `test_parse_music` function contains a test case that creates a music string and an expected output. The actual output is obtained by calling the `parse_music` function with the given music string, and the test asserts that the actual output matches the expected one. 

The `if __name__ == "__main__":` block ensures that the test case is executed only when the script is run directly, not when it's imported as a module.