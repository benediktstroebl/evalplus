```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = ['o', 'o|', '.|']  # will use this list of notes
    beat = 1

    notes = music_string.split(' '|')  # uses split to separate notes by each '|'

    notes = [int(note) for note in notes]  # converts string notes to int

    return [length(note) for note in notes for note in notes if note in notes]  # uses list comprehension

    # tests
    # test string with only whole notes
    test_string = 'oo'
    notes = parse_music(test_string)
    print(notes)
    assert len(notes)==4
    # test string with only half notes
    test_string = 'o|oo'
    notes = parse_music(test_string)
    print(notes)
    assert len(notes)==2
    # test string with mixed notes
    test_string = 'oo|oo . o| o .| .'.'
    notes = parse_music(test_string)
    print(notes)
    assert len(notes)==5
    ```
The code defines a function `parse_music` that takes a music string as input and returns a list of integers representing the duration of each musical note. The function splits the musical notes into different segments using the `split` method, then, it converts each note in the string to an integer. 

Finally, it uses list comprehension and assert statements to test the parsing correctness.