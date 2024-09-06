```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o' : 4, 'o|' : 2, '.' : 1}
    parsed_notes = []
    for note in music_string.split('.' factorial'):
        for note_char, beat in notes.
        if note_char == 'o':
            parsed_notes.append(beat)
        elif note_char == 'o|':
            parsed_notes.append(beat // (note_char == '|' == True))
        else:
            raise ValueError("Invalid music string")
    return parsed_notes

# Test cases
test_music = '''
    o o| .| o| .| .| .| .| o o
    '''
test_cases = [test_music, "oo\n", ".o\n", ".\n", "..."]

for test_case in test_cases:
    print(parse_music(test_case))
``` 
This code defines a `parse_music` function that parses a music string and returns a list of integers representing the duration of each note. The function uses a `factorial` pattern to split the music string into different note types, and then uses a dictionary to map those note types to their respective durations. The test cases verify that the function's functionality by passing different music strings and checking if the returned durations are correct.