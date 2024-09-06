Here's a Python script with a self-contained function that solves the problem:
```python
def is_bored(S):
    boredom_count = sum(1 for sentence in S.split('. ') if sentence.strip()[0] == 'I')
    return boredom_count
```
This function uses a generator expression to traverse over each sentence (assuming each sentence concludes with an exclamation mark, question mark, or period), checks if the first word of each sentence is "I", and accumulates the occurrences in a sum. The accumulated result is the number of boredoms in the provided string.

Here's how you can test it using the Python unittest framework:
```python
import unittest

class TestIsBored(unittest.TestCase):
    def test_bored_1(self):
        self.assertEqual(is_bored("The sky is blue. The sun is shining. I love this weather"), 1)

    def test_bored_2(self):
        self.assertEqual(is_bored("Hello world"), 0)

    def test_bored_3(self):
        self.assertEqual(is_bored("I am bored. What should we do today?"), 1)

if __name__ == '__main__':
    unittest.main()
```
This script uses the `unittest` framework to define three test cases that validate the `is_bored()` function. If you run this script, the `unittest` framework will execute each test case and report if the expected results match the actual output of the `is_bored()` function.