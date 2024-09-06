```python
from typing import List

PATTERN = "[o|o|.|)]"


def parse_music(music_string: str) -> List[int]:
    result = [4, 2, 1]
    for char in music_string:
        if char in 'o|o|.|':
            result.pop(0)
        else:
            result.append(1)
    return result
```

This script includes a list of default values for the `result` list, assuming the shortest note is a quater note that lasts one beat. Then it goes through each character in the input string and if it matches the pattern, it removes the corresponding number of beats from the `result` list. If it doesn't match the pattern, it adds 1 to the list, as this is the default value for each not that doesn't match the pattern. 

Here's an example of how you can run this script with the Jupyter notebook:
```python
import unittest
from parse_music import parse_music

class TestParseMusic(unittest.TestCase):
    def test_parse_music1(self):
        self.assertEqual(parse_music('o o| .| o| o| .| .| .| o o'), [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4])

    def test_parse_music2(self):
        self.assertEqual(parse_music('...|.....'), [1, 1, 1, 1, 1])

    def test_parse_music3(self):
        self.assertEqual(parse_music('o|o|o'), [2, 2, 4])

if __name__ == '__main__':
    unittest.main()
```

If you are using a different IDE, you can add and run tests manually based on this example.