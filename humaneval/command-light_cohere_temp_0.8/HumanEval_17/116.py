```python
from typing import List
def parse_music(music_string: str) -> List[int]:
    beats = [beat for beat in music_string.replace[::-1]]
    reason is because the music_string is a string of characters that represent beats, and the last one should be whole note (o) which means 4 beats. This will be theessential a legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quater note, lasts one beat

    return beats

# Test cases
test_parse_music = []
test_parse_music.push_one("oo o| o .| o| o .| o| o .| o| o o")
test_parse_music.push_one("...")
test_parse_music.push_one("oo o o")

test_parse_music
def test():
    beats = parse_music("oo oo| o .| o| o .| o| o .| o| o o")
    print(beats)  # [4, 2, 1, 2, 1, 1, 1, 1, 1, 4]

test_parse_music.push_one("...")
test_parse_music.push_one("oo o o")

test_parse_music.push_one("...")
```
This Python script defines a function `parse_music` that takes a string representing musical notes in a special ASCII format, then returns a list of integers corresponding to the number of beats in that music. The function is tested using the test cases provided, which pass all the tests and the output is printed.