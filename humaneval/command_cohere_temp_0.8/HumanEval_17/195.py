```python
from typing import List

Pattern = str

def parse_music(music_string: Pattern) -> List[int]:
    beat_conversion = {'o': 4, 'o|': 2, '.': 1}
    return [beat_conversion[note] for note in music_string]
```

The following is a test script that provides an example usage and tests the functionality of the `parse_music` function:
```python
def test_parse_music():
    test_strings = [
        'o o| .| o| o| .| .| .| .| o o',
        'o| .| o| .| .| .| o| o| .| .| 4',
        'o o| .| o| .| .| .| .| .| o o| 4',
        'o .| o| .| o| o| .| .| .| o .| 2',
    ]

    expected_results = [
        [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4],
        [4, 1, 1, 1, 1, 1, 4, 1, 1, 2, 2],
        [4, 2, 1, 1, 1, 1, 1, 2, 2, 1, 4],
        [2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2],
    ]

    for string, expected in zip(test_strings, expected_results):
        beat_counts = parse_music(string)
        assert beat_counts == expected

test_parse_music()
```

The `test_parse_music` function tests the `parse_music` function with multiple test cases. We create a list of test strings and expected results. The `zip` function is used to iterate over each test case and assert the output of the `parse_music` function against the expected result. 

To run the test, you can add the above code as a separate module and execute it using the command `python test_parse_music.py`. Alternatively, you can directly copy the code into the Python environment and run it interactively. 

Ensure that all the test cases are passing successfully before proceeding.  This confirms that the `parse_music` function operates correctly and returns the expected beat counts for different input musical strings.  This problem demonstrates an effective usage of `typing` to enhance code readability and `dict` as a handy data structure for mapping beats to their corresponding musical notes.  It showcases an approach to parsing data from a string using a lookup dictionary and typing for clarity and improved code maintainability.  This type of approach can be applicable when dealing with various data parsing and decoding tasks in a variety of application scenarios.