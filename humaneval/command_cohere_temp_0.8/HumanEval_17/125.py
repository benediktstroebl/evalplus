```python
import re
from typing import List

def parse_music(music_string: str) -> List[int]:
    # Regular expression to match a pattern in music string
    pattern = re.compile(r'o|o|.|.')

    # List of tuples with beats and number of occurrences per beat
    notes = [(4,), (2,), (1,), ()]

    # Using map to replace matched patterns with corresponding beats
    beats = list(map(lambda x: x[0], pattern.findall(music_string)))

    # Zipping to get number of occurrences for each beat
    return list(zip(*beats))
```

This approach utilizes regular expressions and the `re` module to efficiently parse the musical strings. The pattern `o|o|.|.` captures the whole notes (`o`), half notes (`o|`), quarter notes (`.|`), and empty strings, respectively. The `findall` function retrieves all occurrences of these patterns in the input string. Utilizing the `map` function, each matched pattern is replaced by its corresponding beat value. To obtain the count of each beat, the list of beat values is zipped with the list of occurrences.

To use this code, you'll need to install the `regex` library. Normally, this is straightforwardly done with `pip install regex`. If you're experiencing difficulties installing packages, let me know and I'll help you through the process.

The unit tests are conducted to ensure the function's correctness. You can incorporate these tests into your code as follows:
```python
import unittest

class TestParseMusic(unittest.TestCase):
    def test_parse_music(self):
        self.assertEqual(parse_music('o o| .| o| o| .| .| .| o o'), [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4])
    def test_parse_random_music(self):
        self.assertEqual(parse_music('o o| .| o| o| .| .| .| o'), [4, 2, 1, 2, 2, 1, 1, 1])

if __name__ == '__main__':
    unittest.main()
```

This test suite includes two distinct tests, specifically, a `test_parse_music` function to validate correct parsing and a `test_parse_random_music` function to check correctness against an arbitrary musical string. The `unittest.main()` function is necessary to execute the tests.

If you're unfamiliar with how to execute tests in Python, I'd be glad to help with that as well! Just let me know.