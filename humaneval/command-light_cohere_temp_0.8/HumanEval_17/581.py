```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = music_string.split(' ') ')
    separated_by_bar = [int(note) for note in notes if note.split(' ')[0] == 'o' and note. grouped not note]
    notes: [len(notes) // 4, len(notes) % 2, len(notes) // 1]]
    return notes

# Test cases
tests = [parse_music('o o| .| o| .| .| .| .| o o'), [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4], [0, 4, 0, 0, 0], [0, 0, 0, 4, 0, 0, 0, 4, 0, 0])

# Test result expectedness
def test_parser_music(test_cases, expected_results, test_description):
    for idx, test_case in enumerate(test_cases):
        result = parse_music(test_case)
        assert result == expected_results[idx], f"Error in test case {idx+1}: {test_description}"
    return test_description

print(test_parser_music(tests, [4, 2, 1, 2, 2, 1, 1, 1, 4, 4], ["Test music."], "Test passed."))
``` 
The provided Python script defines a function `parse_music` that takes a string music_string as input and aims to split it into musical notes represented as ASCII characters. The function then parses these notes, where each note is either a whole note 'o' lasting four beats or a half note 'o|' lasting two beats, or a quarter note '.|' lasting one beat. The function splits the input by spaces and then filters out non-musical notes, resulting in a list of note lengths corresponding to the number of beats in each note. The function is then tested using several test cases, and the expected output is compared against the actual output. The script also provides a expected output for each test case.