```python
from typing import List
def parse_music(music_string: str) -> List[int]:
    notes = {'o': 4, 'o|': 2, '.|': 1}
    music_notes = music_string.split(' ')
    precise = []
    for note in music_notes:
        if note.split(' ')[0] in notes:
            precise.append(notes)
        else:
            print(f'Error: unknown note "{note}" found', note)
            return []
    return precise
# Test the function
test_strings = [
    'o o| .| o| .| .| .| .',
    'o o|   .| o| .| .| .| .',
    'o o o o| .o| .| o| .o',
    '---|---|---|---|---|---|',
]

correct_answer = [
    [4, 2, 1, 2, 1, 1, 1, 1, 4, 4],
    [4, 2, 1, 2, 1, 2, 1, 4, 4],
    [4, 2, 1, 1, 2, 4, 4, 4, 4],
    [1, 4, 1, 4, 4, 4, 4]
]

for string in test_strings:
    print(parse_music(string))
    print(correct_answer == parse_music(string))
``` 
The above code defines the function `parse_music` that takes a string of music notes, split the string by spaces, and then parse those notes into a list of beats. It then prints a precise answers to the test cases and checks if the output of the function is correct.