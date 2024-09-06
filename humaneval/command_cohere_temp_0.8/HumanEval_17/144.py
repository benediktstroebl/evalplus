```python
from typing import List

pattern = '^ {0,2}(?:o|o|)|(?:.|\.|)')
regex = re.compile(pattern)

def parse_music(music_string: str) -> List[int]:
    return [int(group().replace('.', '')) for group in regex.findall(music_string)]
```

The crucial part is regular expression pattern `^ {0,2}(?:o|o|)|(?:.|\.|)`. It's designed to match one of the following:
1. `o` or `o` (repetition is allowed 0 or 1 time)
2. `|` (with any amount of optional whitespace around)
3. `.` or `\.` (repetition is allowed 0 or 1 time)

Testing script:
```python
import unittest
from typing import List

from markdown_thought_experiment.parse_music import parse_music

class TestParseMusic(unittest.TestCase):
    def test_example(self):
        music = 'o o| .| o| o| .| .| .| .| o o'
        self.assertEqual(parse_music(music), [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4])

    def test_only_whole_notes(self):
        music = 'oooooooo'
        self.assertEqual(parse_music(music), [4, 4, 4, 4, 4, 4, 4, 4, 4])

    def test_only_half_notes(self):
        music = 'o|o|o|o|'
        self.assertEqual(parse_music(music), [2, 2, 2, 2, 2])

    def test_only_quarter_notes(self):
        music = '.|.|.|.|'
        self.assertEqual(parse_music(music), [1, 1, 1, 1, 1])

    def test_random_combination(self):
        music = 'o o| .| o| o| .| .| .| o| o| o'
        self.assertEqual(parse_music(music), [4, 2, 1, 2, 2, 1, 1, 1, 4, 4])

    def test_empty_string(self):
        self.assertEqual(parse_music(''), [0])

    def test_single_note(self):
        cases = ['o', '|', '.']
        for c in cases:
            with self.subTest(note=c):
                self.assertEqual(parse_music(c), [4, 2, 1])

    def test_invalid_input(self):
        invalid_cases = ['o o', 'o|', '.|.'],
        for c in invalid_cases:
            with self.subTest(music=c):
                with self.assertRaises(ValueError):
                    parse_music(c)

if __name__ == '__main__':
    unittest.main()
```

The test suite contains 11 tests, 10 for specific cases, and 1 for checking if the function raises a `ValueError` for invalid inputs (as indicated by the `assertError` method). Would you like to know more about any of the tests or the code functionality?

Let me know if you'd like to proceed with another problem or question!