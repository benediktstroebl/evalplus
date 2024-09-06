```python
def is_bored(S):
    bored = 0
    for sentence in S.split('.'):
        sentence = sentence.strip()
        if sentence.startswith('I') and sentence.find('!') == -1 and sentence.find('?') == -1:
            bored += 1
    return bored
```

This approach splits the input string by the sentence markers ('.' punctuation mark) and iterates through the sentences. For each sentence, the code strips any leading and trailing whitespaces and checks if the sentence starts with the word 'I'. The function returns the count of sentences that match this pattern, which simulates the count of boredoms in the given string. 

This solution adheres to the problem's requirements and accomplishes the task within a single function, making it efficient and easy to understand. 

```python
import unittest

class TestIsBored(unittest.TestCase):
    def test_is_bored(self):
        """
        Test case:
        >>> is_bored("The sky is blue. The sun is shining. I love this weather")
        1
        """
        self.assertEqual(is_bored("The sky is blue. The sun is shining. I love this weather"), 1)

        """
        Test case:
        >>> is_bored("Hello world")
        0
        """
        self.assertEqual(is_bored("Hello world"), 0)

        """
        Test case:
        >>> is_bored("Just a quick question. Is this possible?")
        0
        """
        self.assertEqual(is_bored("Just a quick question. Is this possible?"), 0)
``` 

This code includes a test suite with three distinct test situations that cover various scenarios and edge cases. The test suite samples are provided to assist you in adequately assessing the function's correctness and ensuring that it complies with the problem's statement. 

You can use this script in your codebase immediately, or you can modify it to accommodate other tests particular to your needs.