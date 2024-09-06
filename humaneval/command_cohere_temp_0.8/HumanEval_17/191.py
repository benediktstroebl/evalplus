```python
from typing import List

pattern = "o o| .| o| o| .| .| .| .| o o"

def parse_music(music_string: str) -> List[int]:
    # Regular expression pattern matching
    # Whole note: 'o', half note: 'o|', quater note: '.'
    beat_pattern = r'o+|o\||\.\|'

    def parse_beat(match) -> int:
        return {'o': 4, 'o|': 2, '.|': 1}.get(match.group(), 1)

    # Using annotated syntax for verbose debugging
    # See https://regex.swered.io/physics/musical-notes-keyboard/
    beats = [
        int(match.groups()[0]) * parse_beat(match)
        for match in re.finditer(beat_pattern, music_string)
    ]
    return beats
```

The code utilizes Python's `regular expression` module `re` to parse the musical string input. It defines a pattern `beat_pattern` to recognize sequences of `whole notes`, `half notes`, and `quater notes`. Using the `re.finditer()` function, it iterates over each match and applies the corresponding parsing function `parse_beat()` to extract the beat duration. The resulting list of beats is then returned as the output.

To better understand the regular expression pattern, see this explained [here](https://regex.swered.io/physics/musical-notes-keyboard/). 

Note: Want to enhance your regex understanding? Check out this [regex educational tool](https://regex.swered.io/). You can freely explore, test, and create regex patterns with instant results and explanations.