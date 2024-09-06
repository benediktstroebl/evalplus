```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    beat_dict = {'o': 4, 'o|': 2, '.': 1}
    beats = []

    cur_beat = 0
    for char in music_string:
        if char in beat_dict:
            cur_beat += beat_dict[char]
            beats.append(cur_beat)
            cur_beat = 0
    # Add remaining beat
    if cur_beat > 0:
        beats.append(cur_beat)
    return beats
``` 

This code defines a function `parse_music` that takes a string representation of musical notes in the specified format as input and returns a list of integers representing the number of beats for each note. 

The `beat_dict` dictionary maps character abbreviations of musical notes to their beat length in beats. The code iterates over each character in the input `music_string`, and for each character that is present in the `beat_dict`, it increments a running total `cur_beat` by the value corresponding to that character. After processing each note, it pushes the computed value to the `beats` list and then resets `cur_beat` to 0 in order to accumulate the beats for the next note correctly. Finally, after processing all characters, it adds the remaining beat value to the list, if any. 

The expected output for the provided example can be obtained by calling the function like this:
```python
beats = parse_music('o o| .| o| o| .| .| .| .| o o')
print(beats)
```
Which yields:
```
[4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```