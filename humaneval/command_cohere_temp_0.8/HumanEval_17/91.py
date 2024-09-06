```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    MOD = 4  # the base duration (whole note)
    beat_durations = {'o': 4, 'o|': 2, '.|': 1}

    result = []
    current_beat = 0
    for char in music_string:
        if char in beat_durations:
            current_beat += beat_durations[char]
            result.append(current_beat)
        else:
            current_beat = (current_beat + MOD) % MOD
    return result
``` 

This code defines a function `parse_music` that takes a string representing musical notes in the given format and returns a list of integers representing the number of beats for each note. 

The `beat_durations` dictionary is created to map each possible note type to its beat duration, where the `MOD` variable is the base duration of a whole note. The algorithm iterates through the input string, accumulating a `current_beat` variable based on the note types encountered, appropriately modulated by the `MOD` value to ensure the beats increment as expected. Using basic ASCII characters, this approach efficiently parses the input string to produce the desired list of beat durations. 

This solution assumes that the input string contains only the note characters specified in the provided example. If the input may contain different characters or variations, the code may need additional handling and validation.