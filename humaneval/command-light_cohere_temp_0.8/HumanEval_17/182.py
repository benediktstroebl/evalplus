```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o' : 4, 'o|' : 2, '.' : 1, 'o' : 4}
    beats = music_string.split('|')
    full_score = []
    for beat in beats:
        pattern = beat.split(' ')')
        pattern = [i.strip() for i in pattern]
        note = pattern[0]
        beats = pattern[1:]
        full_score.append(beats)
    return full_score

# Test cases
test_music_string = 'o o| .| o| .| .| .| .| o o'  # 4 4 2 2 2 1 1 1 1 4 4'
test_case1 = parse_music(test_music_string)
print(test_case1) # [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```
The function parse_music takes a string music_string as input and returns a list of integers. It does this task of parsing the string of musical notes and beats and returning the corresponding score. The test cases demonstrate the test of this function, passing different music strings and printing the resulting scores.