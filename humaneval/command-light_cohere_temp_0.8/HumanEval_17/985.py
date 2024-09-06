Below is a self-contained Python function that parses and converts music note values in a string representation to a list of integers:
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    beats = {}

    # 'o' is whole note, lasts 4 beats
    beats['o'] = 4

    # 'o|' is half note, lasts 2 beats
    beats['o|'] = 2

    # '.|' is quarter note, lasts 1 beat
    beats['.|'] = 1

    # Parsing loop that uses a sliding window approach
    for note, duration in music_string.split(' o| '.|'):
        if note in beats:
            beats[note] = beats[note] + duration

    return list(beats.  # Convert theblist() to a list
```
This function takes a string music_string as input and returns a list of integers. Each integer corresponds to how many beats does each note last according to the dictionary `beats`. The function first defines the dictionary `beats` where the keys are different musical note values and the corresponding values are the durations in beats. Then, the function iterates through the music_string and extracts each note and its duration value. Using the sliding window approach, it addss the duration to the current value of the corresponding note in the dictionary `beats`. Finally, the function returns a list of all the values in the dictionary `beats`.