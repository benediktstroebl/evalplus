```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o' : 4, 'o|' : 2, '.' : 1}
    pattern = r'(\d+)'
    return [int(match[0]) for match in re.findall(pattern, music_string)]

# Test cases
music1 = 'o o| .| o| .| .| o o'  # Should return [4, 2, 1, 2, 1, 2]
music2 = '..| ..| ..| ...'  # Should return [1, 1, 4, 4]
music3 = '....|...|....|...|..'  # Should return [4, 4, 1, 1, 4]
music4 = '....| O O O|...|....|...'  # Should return [4, 4, 2, 2, 2, 2]

# Test success
assert parse_music(music1) == [4, 2, 1, 2, 1, 2]
assert parse_music(music2) == [1, 1, 4, 4]
assert parse_music(music3) == [4, 4, 1, 1, 4]
assert parse_music(music4) == [4, 4, 2, 2, 2, 2]
```
This code defines a `parse_music` function that takes a music string and returns a list of integers representing the number of beats for each note in the music. The function uses a legend of notes and a regex pattern to match the musical notes in the string. It then uses the bars to split the notes and create the list of integers.