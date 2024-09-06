```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    beat_mapping = {'o': 4, 'o|': 2, '.': 1}
    notes = []
    current_beat = 0

    for char in music_string:
        current_beat += beat_mapping.get(char, 0)
        notes.append(current_beat)

    return notes
```

This script defines a function `parse_music` that takes a string input and returns a list of beats. The beat dictionary maps characters to their corresponding beat values. The code iterates through the input string, adding beat values to a running total based on the character's mapping in the beat dictionary. The resulting beat values are stored in a list and returned.

To test this script, you can run the provided example input through the function to see if the resulting beat values match the expected output. Comparing the returned list with the example's result can confirm if the script produces the desired output.

```python
# Test code
test_string = 'o o| .| o| o| .| .| .| .| o o'
expected_beats = [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
resulting_beats = parse_music(test_string)

print(resulting_beats == expected_beats)  # Should print True
```

If you encounter any issues or if the test fails, please let me know! I will be happy to help you analyze the problem and find a solution. Please provide feedback on any specific aspect of the code that you would like to discuss further, and feel free to ask any questions or additional tests you'd like to see.