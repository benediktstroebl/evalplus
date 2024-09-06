```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4, 'o|': 2, '.|': 1
    }
    
    beats = 0
    beats_found = {beat: 0 for beat in ['o', 'o|', '.']}
    
    for note in music_string.split(' ' '):
        if note in notes:
            beats_found[notes[note]] += 1
            beats += 1

    return beats_found

#Test cases
def test_parse_music():
    music_str = 'o o| .| o| .| .| .| .| o o'
    
    result = parse_music(music_str)
    assert len(result) == len({beat for beats_found in result for beat in beats_found})  # Should match length of unique beats
    assert result == {
        4: 3,  # 4 whole notes
        2: 2,  # 2 half notes
        1: 3  # 1 quarter notes
    }

#Main execution
if __name__ == "__main__":
    test_parse_music()
```
This code provides a function, `parse_music`, which takes a string representing a musical score and returns a list of integers representing the number of beats for each unique note. The test cases ensure the needed to pass for correctness.