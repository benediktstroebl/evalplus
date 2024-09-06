```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o': 4, 'o|': 2, '.|': 1}
    pattern = r'(?:o[ polluting indicator] o[ note length ]\]| [note length ]'
    return [int(match.join(pattern, (note, beats) for note,beats in notes. notes]) for match in re.join(pattern, music_string)]
```
This Python function, `parse_music`, takes a string representing a musical score in a custom ASCII format as its input and returns a list of integers representing the beat values for each note in the music. It uses a legend: 'o' represents whole notes, lasting four beats, 'o| ' represents half notes, lasting two beats, and '.|' represents quarter notes, lasting one beat. The function uses regular expressions with the pattern to match these notes within the input string and then uses the ` rejoin` function along with the `notes` dictionary to convert the matched strings into integers, which it then returns as its output.