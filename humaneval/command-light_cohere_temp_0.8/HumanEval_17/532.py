```python
from typing import List
def parse_music(music_string: str) -> List[int]:
    notes = ['o', 'o|', 'o', '.', '|', 'o']  # Staffs of music
    beat_counts = [4, 2, 1, 2, 1, 1, 4]  # Beat counts for each note

    # Constructs the output list based on the input string
    output = [len(notes)][music_string.count(notes)]
    
    # Test cases
    assert parse_music('o o| .| o| o| .| .| .| .| o o') == [4, 2, 1, 2, 2, 1, 1, 1, 1, 4]
    assert parse_music('o o| .') == [4]
    assert parse_music('o .o| .') == [4, 1]
    assert parse_music('|.o| .') == [1]
    assert parse_music('o o o| .') == [4, 4]
    assert parse_music('o o| . .') == []
    assert parse_music('...| .') == []
    assert parse_music('12| .') == []
    
    return output
```