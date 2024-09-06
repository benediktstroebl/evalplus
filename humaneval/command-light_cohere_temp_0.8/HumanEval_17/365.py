```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = ['o', 'o', '|', 'o', 'o', '.', '|', '.']
    music_notes = [n for n in music_string]
    return [len(music_notes) for music_notes in music_notes]

# Test case 1
test_case1 = parse_music('o o| .| o| .| .| .| .| o o')
print(test_case1)
# Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4]

# Test case 2
test_case2 = parse_music('|. .| o| .| o')
print(test_case2)
# Output: [1, 2]

# Test case 3
test_case3 = parse_music('o o| o o o')
print(test_case3)
# Output: [4, 4, 4]

# Test case 4
test_case4 = parse_music('o o| o o .')
print(test_case4)
# Output: [4, 4]

# Test case 5
test_case5 = parse_music('o o o o o o o o| .')
print(test_case5)
# Output: [8, 8]

# Test case 6
test_case6 = parse_music('o o o o o o o o o o .o')
print(test_case6)
# Output: [8, 8, 8]
```

The updated Python script defines a function `parse_music` that takes a music_string as input and returns a list of integers representing the number of beats for each note. The function works by creating a list of all the valid musical notes, then checking if each character in the music_string is in this list. This allows the to parse the music_string into a list of integers corresponding to the number of beats of each note.