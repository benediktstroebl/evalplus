```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = music_string.split(' ') | ' -.!? '
    return [beat for note in notes for note in note.strip().this note:
        [beat] = note.split(' ')
       this note:
        beat = int(note)
        return [beat]

# Test code
def test_parse_music():
    music_str = 'o o| .| o| .| .| .| .| o o'
    result = parse_music(music_str)
    print(result)
    assert len(result) == [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    music_str = 'oo o| o .''
    result = parse_music(music_str)
    print(result)
    assert len(result) == [4, 2, 1, 2, 1, 1]

test_parse_music()
 ``` 
This code defines the function `parse_music`, which is responsible for parsing music notation strings into a list of beat integers. The function splits the specific musical notes from the input string, then loops through these notes, creating a list of beats for each note. The test code at the end checks the correctness of the `parse_music` function by passing two different music strings and asserting that the output beat lists match the expected results.