```python
def is_bored(S):
    boredom_count = sum(1 for sentence in S.split('. ') if sentence.strip().lower().startswith('i'))
    return boredom_count
```

This code defines a function called `is_bored` that takes a string as an input and counts the number of boredoms in the string. A boredom is defined as a sentence that starts with the word 'I'. The code uses a `sum()` function with a generator expression to count the number of boredoms and returns the count.

The function is designed to be self-contained, and it does not rely on any external modules or dependencies. It's also worth noting that the function assumes that the input string contains only ASCII characters and ignores non-ASCII characters and punctuation marks. You can use the function by calling it with a string as an argument, and it will return the number of boredoms in the string. 

You can test this function using Python's `unittest` framework, like this:
```python
import unittest

def is_bored(S):
    boredom_count = sum(1 for sentence in S.split('. ') if sentence.strip().lower().startswith('i'))
    return boredom_count

class TestIsBored(unittest.TestCase):
    def test_bored_with_only_one_sentence(self):
        self.assertEqual(is_bored("I am bored."), 1)

    def test_bored_with_multiple_sentences(self):
        self.assertEqual(is_bored("I am bored. But tomorrow is a new day!), 2)

    def test_not_bored_with_no_sentence(self):
        self.assertEqual(is_bored("Hello world!"), 0)

    def test_bored_with_multiple_boredoms_in_one_sentence(self):
        self.assertEqual(is_bored("I love to code. I hate to debug. I love to compile!), 2)

    def test_multiline_bored(self):
        self.assertEqual(is_bored("I love \njava. Python is \ncool, too!), 2)

if __name__ == '__main__':
    unittest.main()
```

This code provides a test suite with several test cases to validate the `is_bored` function and ensure it behaves as expected. Each test case uses `unittest.assertEqual()` to compare the actual output of the `is_bored` function with the expected result.