```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    music_notes = music_string.split(' ')
    that "o" to return [4] beat, and any other character returns beat = 0.
    for note in music_notes:
        if note.split(' ') != ['o':
            beat += 1
            yield beat

# Test cases
tests_music = '''o o| o o| o o| o o o
|. o + bars || + o| o| o| .| .| .| .| .| o o'''
test_parse = parse_music(tests_music)

print(list(test_parse))
``` 
This code defines a function **`parse_music`** which takes in a string of music and returns a list of beats. It works by splitting the into a character, checking that the character is either an "o" which means it's a whole note and returns 4 beats, or any other character, which returns 0 beats. 

This function can then be used to test with different strings of music to see if it works correctly.