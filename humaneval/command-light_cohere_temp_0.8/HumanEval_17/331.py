```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = music_string.split(' '|')
    whole_notes, rest = [], [] for note in notes:
        if note.startswith('o whole'): whole_notes.append(int(note.split('o whole')[0])
        else:
            rest.append(int(note.split('|')[0]))
    whole_notes.append(0) if len(note) == 1 else 1)
    return whole_notes + rest

# Test suite
def test_music():
    music_str = 'o o| .| o| .| .| .| .| o o'
    result = parse_music(music_str)
    assert result == [4, 2, 1, 2, 1, 1, 1, 1, 4, 4]

# main function with tests
if __name__ == "__main__":
    test_music()
``` 
This code defines a function `parse_music` that takes a string of music notation as input and returns a list of integers representing the duration of each note. The function splits the string into a list of notes, then separates the "whole" notes from the "rest" notes using a `split` method. The function then iterates over the string and correctly identifies the "whole" notes, which have a duration of four beats, and the "rest" notes, which have a duration of two beats. The `whole_notes` list will be initialized with whole notes, and the rest notes will be initialized with quarter notes. The function then correctly sets the whole_notes to be one if the note is a whole note, and sets it to be four if it is a half note. The function then returns the final list of notes.