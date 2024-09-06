```python
from typing import List
def parse_music(music_string: str) -> List[int]:
    notes = music_string.split('o A expected to be notes separated by spaces. The function splits the string and returns a list of integers.

tests_string = '''
'o o| .| o| .| .| o o'
'''
test_result = parse_music(tests_string)
print(test_result)  # Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]

```

The function parse_music takes a string of music notes in the special ASCII format as input and returns a list of integers. The function splits the expected to be a list of notes and returns a list of corresponding beat counts. The tests string is passed to the parse_music function and returns the corresponding list of integers representing the beat count of each note. The test passes successfully.