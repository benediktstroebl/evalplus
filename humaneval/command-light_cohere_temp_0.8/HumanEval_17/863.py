```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o': 4, 'o|': 2, '.|': 1}
    beat_counts = [notes[ch] for ch in music_string.split(' '|')]
    beats = [len(music_string[i:]) for i, ch in enumerate('o|'.split(' '))]
    return beat_counts

# Test cases
test_cases = [
    ("o o| .| o| .| .| .| o o"),
    ("..| .| .| .| .| .| ."),
    ("ooo", None),
]

results = {}
for case in test_cases:
    try:
        beats = parse_music(case)
        if beats is not None:
            results[case] = beats
        else:
            results[case] = "Error"
    except ValueError as e:
        results[case] = str(e)

print("Test Cases:", results)
print("\n")

```
The code defines a function called `parse_music` that takes a string of music notes in a special ASCII format as input and returns a list of integers representing the number of beats for each note. It uses a also defines a dictionary of note characters with their beat durations. The test cases are also defined to verify the functionality of the `parse_music` function. 

The test cases are passed to the `parse_music` function, and the results are stored in a dictionary called `results`. The script then prints out the test cases and their corresponding results.