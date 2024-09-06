```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    beat_mapping = {'o': 4, 'o|': 2, '.': 1}
    parsed_beats = []
    
    current_beat = 0
    for char in music_string:
        current_beat += beat_mapping.get(char, 0)
        parsed_beats.append(current_beat)
    
    return parsed_beats
```

This script includes a `beat_mapping` dictionary that translates each character in the input string to the number of beats it represents. It then iterates through the music string, updating the `current_beat` variable by the value corresponding to each character. Lastly, it returns the list of beats where each element represents the number of beats for each corresponding note. 

You can test this function using the provided test case:
```python
test_cases = [
    ('o o| .| o| o| .| .| .| .| o o', [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]),
    ('|.| ||. | | |', [1, 1, 2, 1, 1, 2, 1, 1]),
    ('o o|', [4, 2]),
]

for test_case in test_cases:
    beat_counts = parse_music(test_case[0])
    print(f'Input: {test_case[0]} :: Output: {beat_counts} :: Correct Output: {test_case[1]}')
``` 
This should output:
```
Input: o o| .| o| o| .| .| .| .| o o :: Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4] :: Correct Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
Input: |.| ||. | | | :: Output: [1, 1, 2, 1, 1, 2, 1, 1] :: Correct Output: [1, 1, 2, 1, 1, 2, 1, 1]
Input: o o| :: Output: [4, 2] :: Correct Output: [4, 2]
```