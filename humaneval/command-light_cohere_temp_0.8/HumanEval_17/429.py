Below is a self-contained Python function that parses a string of musical notes in a special ASCII format into a list of integers representing the number of beats of each note. 

```python
import typing


def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4,  # whole note
        'o|': 2,  # half note
        '.|': 1  # quarter note
    }
    result = []
    beats = 0
    for note in music_string:
        beats += notes[note]
        result.append(beats)
    return result
```
This function, `parse_music`, takes a string music_string as input and iterates over each character in the string. It uses a specific mapping of characters to the number of beats for each note, and then appends the total number of beats for that note to the result list.