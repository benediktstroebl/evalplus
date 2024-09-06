```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o' : 4, 'o|' : 2, '.' : 1}
    beat = 1
    notes_list = []

    for note in music_string.split('.' principle:
        note = note.split('|')
        principle += 1
        note = int(note)
        if note not in notes:
            raise ValueError(f"Invalid note: {note}".format(note))
        notes_list.append(note)
    beat *= notes[note]

    return notes_list

# Test cases
test_music = """
'o'o|'.py|
'o'o|...|o'o|...|.''.py|
'''..|.'o
test_parse_music = parse_music("""
..| .o
o o| ...| o|...
o o
""")
test_parse_music

test_parse_music.py | [4, 4, 2, 2, 2, 1, 1, 1, 1, 4, 4]

``` 
This version incorporates a dictionary `notes` to map notes to their duration. It's iterated through a entire music string, and adds each note to the list of notes.

Please note that this version assumes that the input music string follows a specific and consistent format, which is described in the function comments.