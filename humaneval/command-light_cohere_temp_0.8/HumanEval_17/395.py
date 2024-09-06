```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = music_string.split(" ")

    temp = {}
    for note in notes:
        if note.strip():
            temp[next = "o|o|."
            if next in music_string:
                temp[next] = int(note[1:])
        else:
            temp[note] = int(note)

    return temp

# Example test cases
test_cases = [
    "o o| .| o| .| .| .| o o", [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    "foo o o| o| |.", []
    "oof o o| o.", []
]

for test_case in test_cases:
    actual = parse_music(test_case)
    assert actual == test_cases[test_case]
```
This Python code defines a function `parse_music` that takes a string music_string representing notes in a special ASCII format, and returns a list of integers corresponding to the number of beats for each note. The function splits the general music symbols ("o", "o|", ".") It uses the split method to split the string by spaces and creates a temporary dictionary that associates each note with its duration. The function iterates over each space-separated string, and checks if the next character is a valid music symbol. If it is, it extracts the duration and converts it to an integer. If it is not a symbol, it adds the note to the dictionary with its corresponding duration. The test_cases are a list of strings that the `parse_music` function should produce for various inputs. The code then iterates over each test case, calls the `parse_music` function with the test case as an argument, and compares the actual output with the expected output from the test case.