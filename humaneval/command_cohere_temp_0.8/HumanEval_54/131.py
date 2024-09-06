Here's a Python script with a self-contained function that solves the problem:
```python
def same_chars(s0, s1):
    return len(set(s0) & set(s1)) / min(len(s0), len(s1)) > 0.6
```
The function works by comparing the unique characters in both strings and checking whether common characters make up at least 60% of the shorter string length. The markdown code block for the tests is:
```
```python
import unittest

def same_chars(s0, s1):
    return len(set(s0) & set(s1)) / min(len(s0), len(s1)) > 0.6

class TestSameChars(unittest.TestCase):
    def test_example_1(self):
        self.assertTrue(same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc'))

    def test_example_2(self):
        self.assertTrue(same_chars('abcd', 'dddddddabc'))

    def test_example_3(self):
        self.assertTrue(same_chars('dddddddabc', 'abcd'))

    def test_example_4(self):
        self.assertFalse(same_chars('eabcd', 'dddddddabc'))

    def test_example_5(self):
        self.assertFalse(same_chars('abcd', 'dddddddabce'))

    def test_example_6(self):
        self.assertFalse(same_chars('eabcdzzzz', 'dddzzzzzzzddddabc'))

if __name__ == '__main__':
    unittest.main()
```

To ensure that the function works appropriately in different scenarios, it is vital to provide various test cases that cover a wide range of situations, including matching strings of different lengths and letters, matching strings with different arrangements of the same characters, and verifying that the threshold criterion works correctly.

The output of the test runner will indicate whether the tests passed successfully after executing this code.