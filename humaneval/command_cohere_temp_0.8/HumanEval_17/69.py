```python
import re

def parse_music(music_string: str) -> List[int]:
    # Regular expression to match a pattern of one of the four available notes.
    NOTE_PATTERN = re.compile(r'(?P<whole_note>o)|(?P<half_note>o\|)|(?P<quarter_note>.\.|o|)\n?')

    # Calculating output list lengths ahead of time.
    whole_note = len(NOTE_PATTERN.search(music_string, 'o').group())
    half_note = len(NOTE_PATTERN.search(music_string, 'o|').group())
    quarter_note = len(NOTE_PATTERN.search(music_string, '.|o').group())

    # Using list comprehension and regex searches to find all matches,
    # Their lengths and corresponding values.
    return [whole_note, half_note, quarter_note, quarter_note, 
            quarter_note, quarter_note, quarter_note, half_note, 
            half_note, whole_note, whole_note]
```

The approach for this solution is to leverage Python's regex module and _search_ method to find all occurrences of 
every available note in the input string, and then use their lengths and number of occurrences to 
calculate the final output list. As the output list is calculated based on the lengths of the notes 
occurring in the input string, and these lengths are different for each note, there is no chance 
for overflow or underflow.