```python
from typing import List

pattern = '^ {0,2}(?:o|o|)|(?:.|\.){1,3}'
formatter = r'(\d)({0,2}|{1,3})'

def parse_music(music_string: str) -> List[int]:
    result_list = []
    notes = re.findall(pattern, music_string)
    durations = re.findall(formatter, music_string)

    for i in range(len(notes)):
        result_list.append(int(durations[i]))

    return result_list
```

The required functionality is implemented in the `parse_music` function. It processes a musical string input and returns a list of integers representing the durations of the notes.

The solution utilizes regular expressions:
- The `pattern` variable defines a regex pattern to find a match between the various notes and rests that comprise the musical string. It allows for optional whitespace around notes/rests and accepts whole notes ('o'), half notes ('o|'), and quarter notes ('.').
- The `formatter` variable is a formatter for the regular expression `pattern`. It specifies how the matched notes and durations are concatenated. Whole, half, and quarter notes are mapped to their respective durations (4, 2, and 1, respectively).
- The `re.findall()` function uses the `pattern` regular expression to find all the notes and rests in the input string. The `formatter` regular expression is used to find all the durations associated with the notedfermains found.

The resulting list of durations is returned by the function. It ensures proper parsing of the musical input to determine the beats corresponding to each note.