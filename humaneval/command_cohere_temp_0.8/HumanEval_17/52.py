```python
from typing import List

PATTERN = "o|o|.|"

def parse_music(music_string: str) -> List[int]:
    res = []
    curr_beat = 4
    for note in music_string:
        if note == 'o':
            res.append(curr_beat)
        elif note == '|':
            curr_beat //= 2
        elif note == '.':
            res.append(curr_beat // 4)
        curr_beat //= 4
    return res
```

The algorithm for parsing music strings is as follows:
1. The function iterates through each character in the input string `music_string`.
2. Each musical note is either an 'o', '|', or '.'. These characters represent whole notes, half notes, and quarter notes, respectively.
3. The current beat (valued at 4) is accumulated if the current note is an 'o'. The beat value is added to the list of beats. 
4. If the note is a '|', the current beat is divided by 2, halving its value. This simulates halving the duration of the note. 
5. If the note is a '.', the current beat is divided by 4, as quarter notes are half the duration of a half note. This value is then added to the list of beats. 
6. The current beat value is updated to the new value after each division. 
7. The process repeats for each character in the `music_string`, generating a list of beats that represents the duration of each note in the provided music string. 
```python
# Example usage
music_string = "o o| .| o| o| .| .| .| .| o o"
print(parse_music(music_string))
```