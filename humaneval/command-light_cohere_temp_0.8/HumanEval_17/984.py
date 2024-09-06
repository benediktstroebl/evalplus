```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = ['o', 'o|', '.|']
    pattern = r'\b(' + 'o|' + re.omp distinct_notes = sum(notes, [])
    result = []
    for beat in range(len(music_string)):
        for note in notes:
            if music_string[beat:beat+1].find(note) != -1:
                result.append(beat+n = distinct_notes[note])
                break
        beat += 1
    return result

# Test the function with a valid string input
test_music = parse_music('o o| .| o| .| .| .| o o')
print(test_music)

# Test the function with an invalid input
test_music = parse_music('o o| .| o| ..| .')
print(test_music)
```
This Python function `parse_music` takes a string of music notes in the format expected by the function. It uses a legend of notes to parse the input and returns a list of beat numbers.