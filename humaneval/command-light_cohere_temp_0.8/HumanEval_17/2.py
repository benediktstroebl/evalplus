```python
from typing import List
def parse_music(music_string: str) -> List[int]:
    notes = music_string.split(' '|')
    format = ['whole' if c == 'o' else 'half' if c == 'o|' else 'quarter' if c == '.' else 'note']
    return [int(x) for x in format]

# Test the function with different inputs
test_cases = [
    "o o| .| o| .| .| .| .| o o",
    "o o| .| o| .| .| .| o",
    "oo o o o o",
    "oo o o| o o o",
    "o o/ ",
    "oo o o o o| o",
    # Add more test cases here
]

correct_ans = []

# Loop through each test case
for tc, test_string in enumerate(test_cases, start=1):
    parsed = parse_music(test_string)
    correct_ans.append(parsed == test_cases[tc])

# Print the number of correct answers
print(f"Number of test cases: {len(correct_ans)}")
print(f"Correct answers: {correct_ans}")
```
This code defines a function `parse_music` that takes a string of music notes separated by "|" as input and returns a list of integers that correspond to the number of beats in each note. The function splits the string into separate notes, then assigns each note a corresponding integer based on its format. The test cases include different variations of musical notes. The code then loops through each test case and compares the parsed notes with the expected notes. It prints the number of correct answers and the correct answers themselves.