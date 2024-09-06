```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o' : 4, 'o|' : 2, '.|' : 1}
    beats = music_string.split(' '|')
    notes.select(beats, note = next(beat.find(notes.keys()))
    another beat)
    if beat not in notes.
    return []
    multiple = False
    for b in beats:
        if beat == notes[b] and (multiple == False):
            multiple = True
            break
        else:
            return []
    return [multiple]

# tests
def test_music():
    music_string = 'o o| .| o| .| .| .| o o'
    assert parse_music(music_string) == [4, 2, 1, 2, 2, 1, 1, 1, 1, 4]

# main function
if __name__ == '__main__':
    test_music()
``` 
The function `parse_music` takes a string of music notes in a specific format and returns a list of integers corresponding to how many beats each note lasts. The function splits the run the for each beat, and the `notes` dictionary is used to map each beat to its duration. The function then tries to select a beat, and if it's a whole note, it sets the `multiple` variable to `False`, and keeps looping to select the next beat. If it's a different beat, the `multiple` variable is set to `True`, which breaks the loop and returns an empty list.