```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    beat_map = {'o': 4, 'o|': 2, '.|': 1}
    result = []
    current_beat = 0

    for char in music_string:
        current_beat += beat_map.get(char, 0)
        result.append(current_beat)

    return result
``` 

This script defines a function `parse_music` that takes a string representing musical notes in the specified format and returns a list of integers representing the number of beats for each note. The beat map helps to associate each character with its beat length. The function iterates over the input string, accumulating the beat count using the beat map, and stores the resulting beats in the resulting list. 

To test this script, you can use the example input provided in the problem statement, and the expected output `[4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]` should be returned. 
To test the function, you can call it and pass different strings representing musical notes in the specified format as input, and verify that the returned list of integers matches the expected output. 
For automation of this process, you can use Python's `unittest` module to automate testing your function with different inputs. Here is an example test class `TestParseMusic` that can be used to verify your solution:
```python
import unittest
from parse_music import parse_music

class TestParseMusic(unittest.TestCase):
    def test_example(self):
        self.assertEqual(parse_music('o o| .| o| o| .| .| .| o o'), [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4])

    def test_whole_notes(self):
        self.assertEqual(parse_music('oooooooo'), [4, 4, 4, 4, 4, 4, 4, 4, 4, 4])

    def test_half_notes(self):
        self.assertEqual(parse_music('o|o|o|o|'), [2, 2, 2, 2, 2])

    def test_quarter_notes(self):
        self.assertEqual(parse_music('.|.|.+|.+|'), [1, 1, 1, 1, 1, 1, 1])

    def test_mixed_notes(self):
        self.assertEqual(parse_music('o o| .| o| o| .| .| .| o o|o |.'), [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 2, 1])

if __name__ == '__main__':
    unittest.main()
``` 
To add these tests into your solution, firstly you need to install flake8 and mypy, and make sure your code passes flake8 and mypy checks. After that, you need to add the `test_parse_music` function to your test file, and then use `unittest.main()` to discover and run the test cases. This way, by running this test file, you can validate your solution and ensure it produces the expected outputs for various inputs.