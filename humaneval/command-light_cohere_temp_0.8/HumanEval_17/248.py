```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o' : 4, 'o|' : 2, '.' : 1}
    
    beats = [notes[ch] for ch in music_string.split('o
                                if 'o' in music_string or ch in music_string.split('o}{ ]: beats.append(0)
    result: beats

    return beats

# Test cases
test_parse_music = [parse_music("oo|oo|oo|oo|oo|oo|oo| .|oo"),  # Should return [4, 2, 0, 0, 0, 0]
                         parse_music("oo| o| o| .| o| .| .| .| .| o o"),  # Should return [4, 2, 1, 2, 1, 1, 1, 1, 1, 4, 4]
                         parse_music("|.| .| .| .| .| o"),  # Should return [1, 0, 0, 0]
                         parse_music(".|.a| ."),  # Should return [0, 0]
                         parse_music("www"),  # Should return []
                         parse_music("aboat"),  # Should return []
                         parse_music("."odad"),  # Should return []
                         parse_music("ac"),   # Should return []
                         parse_music("a c"),  # Should return []
                         parse_music("a #c")  # Should return []
                         ]

# Test case output
print(test_parse_music[0])  # [4, 2, 0, 0, 0]
print(test_parse_music[1])  # [4, 2, 1, 2, 1, 1, 1, 4, 4]
print(test_parse_music[3])  # [1, 0, 0, 0]
print(test_parse_music[4])  # []
print(test_parse_music[6])  # []
```
This Python code defines a function `parse_music` that takes a music string as input and returns a list of integers corresponding to the number of beats in the music. It uses a legend where 'o' represents a whole note, 'o|' represents a half note, and '.' represents a quarter note. The function splits the multiple times of each note in the string and appends the appropriate number of beats for each note. 

This script also provides several test cases to check the correctness of the function, and the expected output of each test case is printed.