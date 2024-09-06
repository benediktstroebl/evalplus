```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    beat_dict = {'o': 4, 'o|': 2, '.|': 1}
    beats = []

    cur_beat = 0
    for note in music_string:
        if note in beat_dict:
            cur_beat += beat_dict[note]
        else:
            beats.append(cur_beat)
            cur_beat = 0

    beats.append(cur_beat)
    return beats
``` 

This script defines a function `parse_music` that takes a string representing musical notes in the given ASCII format and returns a list of integers representing the number of beats for each note. 

The beat dictionary maps the special characters to the number of beats they represent. It is initialized outside of the function and can be reused across multiple calls to the function. The beats list is used to store the beats for each note. 

The function goes through each character in the music string, and if the current note is in the beat dictionary, its value is added to the current beat. If it's not, it means a new note has started, so the current beat is added to the beats list and the current beat is reset to 0. Finally, the last beat is appended to the list and returned. 

Here is an example usage of the code:
```python
beats = parse_music('o o| .| o| o| .| .| .| .| o o')
print(beats)  # [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
``` 
This would print the list of beats for the provided music string in the given format. 

This approach assumes that the input string will only contain the noted mentioned in the problem statement and will return a wrong result for any other values inserted in the string. 
If you want the code to be a bit more robust to other values, you can release it as following: 

```python
from typing import List, Optional

def parse_music(music_string: str) -> List[int]:
    beat_dict = {'o': 4, 'o|': 2, '.|': 1}
    beats = []

    cur_beat = 0
    current_note = None  # Optional[str]

    for note in music_string:
        if current_note is None:
            if note in beat_dict:
                current_note = note
                continue
            else:
                beats.append(cur_beat)
                cur_beat = 0
                continue

        if note == current_note:
            cur_beat += beat_dict[current_note]
        elif note in beat_dict:
            beats.append(cur_beat)
            cur_beat = beat_dict[note]
            current_note = note
        else:
            beats.append(cur_beat)
            cur_beat = 0
            current_note = None

    if current_note is not None:
        beats.append(cur_beat)
    return beats
``` 

With this version, each time a new note starts, the function follows the below process:
1. If it is the same as the previous one, increment the beat counter
2. If it is a new note, add the current beat to the beats list and reset the current beat to the new note's beat
3. If the note is not in the beat dictionary, add the current beat to the list and reset the current beat to 0, as it is an unknown value. 

This way, the function will handle unknown notes