```python
from typing import List

pattern = "o o| .| o| o| .| .| .| .| o o"

def parse_music(music_string: str) -> List[int]:
    beat_dict = {'o': 4, 'o|': 2, '.': 1}
    return [beat_dict[note] for note in music_string]

# Test scenario
print(parse_music(pattern))
```

The function `parse_music` takes a string as input and returns a list of integers representing the number of beats for each note. This function utilizes a dictionary, `beat_dict`, which maps specific notes to their corresponding beat values. It then iterates through the provided `music_string`, using the dictionary to convert each note into its beat value, consequently returning a list of these beat counts. 

The provided test scenario demonstrates the function's application on the given input pattern, printing the resultant beat counts for each note, accordingly.