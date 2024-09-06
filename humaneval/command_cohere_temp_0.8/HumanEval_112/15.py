```python
def reverse_delete(s, c):
    delete = [char for char in c]
    palindrome = s == s[::-1]
    return ('', '') if not s else (s.translate(str.maketrans('', '', delete)), palindrome)
```

This Python script provides a function called `reverse_delete`, which takes two strings as input, `s` and `c`, and returns a tuple with the processed string and a boolean indicating whether the processed string is a palindrome. The task is to remove all characters from string `s` that are present in string `c` and then check whether the resulting string is a palindrome. The `translate` method is used to remove characters from string `s` based on a translation table created using `str.maketrans`. The resulting string is compared to its reverse to determine if it's a palindrome. The function returns '' and '' for false palindrome checks or empty input strings.

Here's an example usage of the function:
```python
>>> reverse_delete('abcde', 'ae')
('bcd', False)
>>> reverse_delete('abcdef', 'b')
('acdef', False)
>>> reverse_delete('abcdedcba', 'ab')
('cdedc', True)
``` 

The unit tests for this function are not included in the script, but they can be added to ensure its correctness. Here's an example of a basic unit test for the `reverse_delete` function:
```python
import unittest

def reverse_delete(s, c):
    delete = [char for char in c]
    palindrome = s == s[::-1]
    return ('', '') if not s else (s.translate(str.maketrans('', '', delete)), palindrome)

class TestReverseDelete(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(reverse_delete('abcde', 'ae'), ('bcd', False))
        self.assertEqual(reverse_delete('abcdef', 'b'), ('acdef', False))
        self.assertEqual(reverse_delete('abcdedcba', 'ab'), ('cdedc', True))

    def test_empty_strings(self):
        self.assertEqual(reverse_delete('', 'a'), ('', True))
        self.assertEqual(reverse_delete('abc', ''), ('abc', True))
        self.assertEqual(reverse_delete('', ''), ('', True))

    def test_palindrome_detection(self):
        self.assertEqual(reverse_delete('abcdedcba', 'ab'), ('cdedc', True))
        self.assertEqual(reverse_delete('abcba', 'ab'), ('acba', True))
        self.assertEqual(reverse_delete('abc', 'a'), ('bc', True))

if __name__ == '__main__':
    unittest.main()
```

In this example, the `TestReverseDelete` class inherits from `unittest.TestCase`, providing various test methods to cover different scenarios of the `reverse_delete` function. Each method tests a specific condition and verifies whether the output of the function is as expected. The `unittest.main()` function is called to discover and run the test cases.