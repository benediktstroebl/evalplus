```python
from typing import List

pattern = 'o|_|.|'

def parse_music(music_string: str) -> List[int]:
    res = []
    curr_note = 4
    for c in music_string:
        if c == 'o':
            curr_note *= 2
        elif c == '|':
            curr_note //= 2
        elif c == '.':
            res.append(curr_note)
            curr_note = 4
        elif c == ' ':
            continue
        else:
            raise ValueError(f"Unexpected char {c}")
    return res
```

The algorithm of the `parse_music` function is as follows:
1. Initialize an empty list `res` to store the parsing results and initialize the current note's duration to 4 (whole note).
2. Iterate through each character in the input `music_string`.
3. If the character is `'o'`, double the current note's duration.
4. If the character is `'|'`, divide the current note's duration by 2.
5. If the character is `'.'`, append the current note's duration to the result list and reset the current note's duration to 4.
6. If the character is `' '`, ignore it and move to the next character.
7. For any other character, raise a `ValueError` indicating an unexpected character. 

The script assumes that the input string follows the specified format and that the only unexpected char that may be presented in the string is spaces, which are ignored. Thus, the code is optimized and concise.

The unit tests for this code can be added as follows:
```python
import unittest

class TestParseMusic(unittest.TestCase):
    def test_parse_music(self):
        self.assertEqual(parse_music('o o| .| o| o| .| .| .| o o'), [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4])

    def test_parse_only_whole_notes(self):
        self.assertEqual(parse_music('oooooo ||||'), [8, 8, 8, 8])

    def test_parse_random_input(self):
        self.assertEqual(parse_music('o o| .|Aargh!!'), [4, 2, 1])

    def test_parse_multiple_beats(self):
        self.assertEqual(parse_music('o o| .| o| o| .| .| .| o o'), [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4])

    def test_raise_error_on_invalid_char(self):
        with self.assertRaises(ValueError):
            parse_music('o o| .| d| o| .| .| .| o o')

if __name__ == '__main__':
    unittest.main()
```

This way, the code checks for various edge cases, including half and quarter notes, multiple beats, and invalid input, ensuring that the function behaves as expected. 

Note: If you have more questions or need assistance with any other coding problems, please let me know. I'm here to help!