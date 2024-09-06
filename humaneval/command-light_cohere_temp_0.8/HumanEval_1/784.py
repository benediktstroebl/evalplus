```python
from typing import List
def separate_paren_groups(parentheses: str) -> List[str]:
    """
    Function to separate and return list of non-nested parentheses.
    Input: 
    - A string of unbalanced parenthesis
    Return: A list of separated strings.
    """
    using list comprehension, we can separate the unbalanced parentheses. The check if the open parenthesis is an average case.
    """
    In the unbalanced case, it will be an average case.
    """
    then, we check if the open parenthesis is followed by a closing parenthesis. If not, we append the current string to the list.
    """ The if the open parenthesis is not followed by a closing parenthesis, we append the current string to the list and follow with the next string. 
```

Here's the test code to verify the function's correctness:
```python
import unittest

class tests:
    unittest.TestCase(__main(__file__))
```

The code above creates a test class with one test case. The `unittest.TestCase` method helps main function.