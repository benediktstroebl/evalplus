```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = music_string.split(' ')').
    notes = [int(x) for x in notes if x.isdigit()]
    verifications = any("o", "o/") in notes
    for note in notes:
        if note == "o":
            note = 4
        elif note == "o/":
            note = 2
        elif note == ".":":
            note = 1
        else:
            raise ValueError("Invalid note encountered.")
    return note

# Test the function
test_music = "o o| .| o| .| .| .| .| o o"
test_value = parse_music(test_music)
print(test_value)

test_music = "!.| .| o| .| o"
test_value = parse_music(test_music)
print(test_value)

test_music = "oo"
test_value = parse_music(test_music)
print(test_value)

test_music = "!".join
test_value = parse_music(test_music)
print(test_value)
```
This Python script defines a function called `parse_music` that takes a string music_string as input and returns a list of integers. The function splits the notes by spaces and then, using list comprehension and the `isdigit()` function, converts the notes to integers. 

The function handles various valid cases of notes, such as whole notes (o), half notes (o/), and quarter notes (.).

To test the function, the script defines a few test cases, each representing a different music note. The test cases are passed to the `parse_music` function and the resulting values are printed. The script also includes a final test case where an empty string is passed, which should return an empty list.