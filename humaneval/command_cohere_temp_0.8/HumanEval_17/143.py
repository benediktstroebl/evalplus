```python
import re

def parse_music(music_string: str) -> List[int]:
    # Regular expression to match a pattern of one of the four notes
    note_pattern = re.compile(r'(?<!\d)(?=o)|(?<!(?=o))(?=.\.|o|o|)')

    # Calculating length of notes from given `music_string`
    beats = [len(note_pattern.findall(line)) for line in music_string.split('\n')]
    return beats
```

The logic here leverages regular expressions to match note patterns within each line of the input string. This effectively calculates the length of each note in terms of beats by counting the occurrences of each note type.

To ensure the regular expression matches only valid note sequences, it specifically looks for either 'o', '.|' or 'o|' that are not preceded by, or followed by any digit. This prevents any potential mismatches with numbers present in the input. 

The returned list of beat lengths corresponds to the number of beats each note lasts.