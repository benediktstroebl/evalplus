```python
from typing import List

PATTERN = "/(?P<whole>o)(?P<half>o|)|(?P<quarter>.)/"

def parse_music(music_string: str) -> List[int]:
    return [
        len(re.findall(PATTERN.format(whole='*' if i % 2 == 0 else '',
                                      half='*' if i % 3 == 0 else '',
                                      quarter='*' if i % 4 == 0 else ''),
                        music_string))
        for i in range(len(music_string))
    ]
```

The Python regular expression pattern `PATTERN` is used to match the various note lengths in the input string. It consists of three capturing groups, separated by the pipe symbol `|`, which matches the start of a new group. These groups define patterns for whole notes, half notes, and quarter notes, respectively.

Whole notes are represented by the character `o` in the input string and have the pattern `o*`, where `*` indicates that they can occur zero or more times. Half notes are represented by `o` or `|` in the input string and have the pattern `o*|` or `|*`, respectively. Similarly, quarter notes are represented by the character `.` in the input string and have the pattern `.*`.

The function `parse_music` takes a music_string as input and returns a list of integers representing the beats of each note. The list is created by using a list comprehension that iterates over each character in the input string. For each character, the regular expression is used to find all matches for that note length in the remaining part of the string using the `re.findall` function. The length of the list of finds corresponds to how many beats the note last.

To pass the test cases, the function is evaluated with example input strings, and the resulting list of beats is compared to the expected output using the `assert` statement.