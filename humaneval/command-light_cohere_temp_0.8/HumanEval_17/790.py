```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    beats = [0] * 7  # Initialize beat counter

    for note in music_string:
        if note == 'o':  # Whole note, lasts 4 beats
            beats[0] += 1
        elif note == 'o|':  # Half note, lasts 2 beats
            beats[1] += 1
        elif note == '.|':  # Quarter note, lasts 1 beat
            beats[2] += 1
        else:
            raise ValueError("Invalid note format")

        if any(beat > 4 for beat in beats):
            raise ValueError("Notes do not last 4 beats")

    return beats

# Test cases
test_cases = [
    ("o o| .| o| .| .| .| o o"),
    ("|.|.#. |.", ".. .|"),
    ("oo|.", "o|." ^ ".|." ^ "|"),
    # Invalid input
]

for test_case in test_cases:
    actual_beats = parse_music(test_case)
    expected_beats = [4, 2, 1, 2, 1, 1, 1, 4]  # Reference beat values

    if actual_beats != expected_beats:
        print(f"Test case {test_case} failed.")
        continue

    print(f"Test case {test_case} passed.")
```
This Python code defines a function called `parse_music` that takes a string of music notes as input and returns a list of integers representing the duration of each note in beats. The code uses the particular ASCII format for notes:

- Whole notes are represented by 'o'.
- Half notes are represented by 'o|'.
- Quarter notes are represented by '|.'

The code also defines a list of test cases with various input strings and expected output lists of beat durations. The code then loops through each test case, it calls the `parse_music` function with the input string and compares the actual output list with the expected output list. If the actual output does not match the expected output, the code prints an error message indicating the failed test case. If the output matches the print the expected output, the code prints a success message for the test case.

Finally, the code runs through all the test cases, and prints the results. The output will show whether the test cases passed or failed based on the comparison of actual and expected output lists of beat durations.