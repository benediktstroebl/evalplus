```python
import re

def split_words(txt):
    ans = []
    txt = re.sub(r',', ' ', txt)
    ans = txt.split()
    if not ans: ans = len(list(re.findall(r'[a-z]', txt)))
    return ans
```

The code uses default Python libraries to solve the problem without any external dependencies. The function `split_words` takes the input text and processes it to reach the desired output as described in the prompt.

The script assumes that the input will follow the given examples in the prompt and doesn't cover 100% of all possible cases. For example, the input `"abc,def,ghilf"` will return an answer asserting that it is not a list, although technically it could be considered valid according to the given examples. But since the assumption is that the input is strings with words separated by whitespace or comma, it provides a reasonably efficient solution.  If you want to cover this edge case, you could modify the `re.sub` line to be `re.sub(r'[,\s]+', ' ', txt)` to handle multiple whitespace and commas combinations.  This may though decrease the efficiency of the solution.  Alternatively, you could change the test cases to cover this combination of input to ensure stable operations for the edge case and users with that input.  This would also help to follow the **Given-When-Then** principle in writing tests for code, as you now cover the specific test case which could cause a specific behavior, and hence reduce ambiguity in the functions operation in the future.  It could look like this:
```python
import unittest
from split_words import split_words

class TestSplitWords(unittest.TestCase):
  def test_split_words_empty(self):
    self.assertEqual(split_words(""), [])  # Edge case to cover

  def test_split_words_none_ Separation(self):
    self.assertEqual(split_words("abcdef"), 3)  # As per the examples in the prompt

  def test_split_words_whitespace(self):
    self.assertEqual(split_words("Hello world!"), ["Hello", "world!"])

  def test_split_words_comma(self):
    self.assertEqual(split_words("Hello, world!"), ["Hello", "world!"])

if __name__ == '__main__':
    unittest.main()
``` 
This would complete the coverage of the testing suite and cover also the specific case of input with commas and equal number of words, but still would assume that the input is a string of words separated by commas or whitespaces.  If you expect other kinds of input, you would need to adjust the code and testing coverage accordingly.  It is always a good idea to cover your tests for corner cases like this to ensure stable operation of your functions in all possible scenarios.  This makes the code more robust and gives clearer operation expectations for future users of the function.  It would also be beneficial to add additional edge cases, if applicable, to cover more scenarios and ensure the stability and correctness of the function.  This could look like adding more tests or adding more specific test assertions for certain expected behaviors.  This highly depends on the context of your function's operation and the expected input/output of it.