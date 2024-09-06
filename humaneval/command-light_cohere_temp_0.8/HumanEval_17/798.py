```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o': 4, 'o|': 2, '.|': 1}
    
    def count_beats(string):
        beats = 0
        for char in string:
            if notes.get(char, None):
                beats += 1
        return beats
    
    music_notes = []
    for beat in range(1, 6):  # Limit the range to ensure only whole notes
        note_duration = 4 if beat in [1, 2] else 2
        note = 'o|' if beat in [1] else 'o'
        music_notes.append(note_duration * count_beats(note))
    
    return music_notes

# Test cases
test_cases = [["o o| .| o| .| .| .", # Different lengths
             "o o| .| o| o| .| .| .", # Different notes
             ".|."  # Quarter note, should return 1 beat
             "ooo".  # Extra characters, should not affect the parsing
             "oo o".  # Extra space, should not affect the parsing]

for test_case in test_cases:
    parsed_notes = parse_music(test_case)
    print(parsed_notes)
``` 
This Python script defines a function `parse_music` that takes a string representing a melody and returns a list of00514 integers. The function `count_beats` is a helper function that counts the number of beats in a music string. 

The function `parse_music` uses a dictionary `notes` that maps musical notes to their duration in beats. The function iterates over the strings and extracts the notes, using the `get` method to check if a character is in the map. The function appends the beats to the note's duration, and adds the result to a list of music notes. 

The script also includes a set of test cases that cover different variations of music strings.