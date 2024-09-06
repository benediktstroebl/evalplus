```python
from typing import List
def parse_music(music_string: str) -> List[int]:
    notes = {'o': 4, 'o|': 2, '.|': 1}
    beats = music_string.split(' '|')
    pattern = ['[' + note + ']'] * (len(beats) - 1) + ['']
    return [int(note) for note in pattern if note in notes]

# Test the function with a variety of inputs
test_cases = [
    'o o| .| o| .| .| .| .| .',
    'o o o o o',
    'o o| .| o',
    'o .| .o',
    'o o o| .|',
    'o o o o',
    '..|..',
    'o 4|5|6',
]

correct_ans = []
for case in test_cases:
    ans = parse_music(case)
    correct_ans.append(ans == [list(range(1, 7)))]

print(f'All test cases passed!')
print(f'Correct answers: {correct_ans}')
```