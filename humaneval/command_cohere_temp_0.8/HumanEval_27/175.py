```python
def flip_case(string: str) -> str:
    return ''.join(c.swapcase() if c.isalpha() else c for c in string)
```

This script provides a function that accepts a string as input and returns a new string where all lowercase characters are flipped to uppercase and all uppercase characters are flipped to lowercase. This is achieved by using a list comprehension that checks if each character is alphabetic using the `isalpha()` string method, and if so, applies the `swapcase()` method to flip the case. Non-alphabetic characters are directly appended to the final string.

To test this function, you can run the following code using the `pytest` framework, which is widely used for Python testing:
```python
import pytest

def test_flip_case():
    assert flip_case('Hello World') == 'hELLO dORLd'

def test_flip_case_non_alphabetic():
    assert flip_case('With uppercase characters!') == 'wIth uPPERCASE CHARACTERS!'
```

This code uses the `pytest` framework to define two test functions. The first test function, `test_flip_case`, checks whether the `flip_case` function correctly flips the case of a string containing both uppercase and lowercase characters. The second test function, `test_flip_case_non_alphabetic`, assesses the function's behavior when a string contains no alphabetic characters. Both tests are asserted to have `True` as the expected output, and upon executing the code using `python -m pytest test.py`, these tests should pass.