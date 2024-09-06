```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    music_notes = music_string.split(' ')
    sharp')
    notes = [int(note.strip(re.match(r'o (['o', 'o', '|', '.'))) for note in sharp]
    return [beat for beat in [4] * notes] + [beat for beat in [2] * notes]

# Test the function
test_music = """
'o o| .| o| .| .| .| .| o o'

o o'

o o|."split(' ')

test_music_ parsed = parse_music(test_music)
print(test_music_parsed)

# Test cases 2 and 3
test_music2 = """
'o o| .|.o .| o

. . note."
. major notes and whole".

test_music3 = """
'o o o| .| o

o o| o| .| .| o

o o o'

"""
test_music_parsed2 = parse_music(test_music2)
print(test_music_parsed2)
```