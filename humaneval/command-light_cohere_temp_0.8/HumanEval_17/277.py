Below is a Python script with a self-contained function that solves the problem of parsing musical notes represented in a string to a list of integers representing the number of beats for each note. 

```python
# A self-contained function that solves the music score parsing problem
def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }
    notes_list = []
    for note in music_string.get():
       
        # Converts each note to a number
        notes_list.append(notes[note])
    return notes_list
```