```python
def correct_bracketing(brackets):
    open_brackets = brackets.count("(")
    close_brackets = brackets.count(")")
    return open_brackets == close_brackets
```

This function counts the number of opening and closing brackets using the `count` method. Then, it returns `True` if the counts are equal, indicating that every opening bracket has a corresponding closing bracket.

Here is a markdown code block demonstrating the unit test using the `pytest` framework:
```python
import pytest

def test_correct_bracketing():
    assert correct_bracketing("()")
    assert correct_bracketing("(()())")
    assert not correct_bracketing(")(()")
    assert not correct_bracketing("")
    assert not correct_bracketing("(()")
``` 

This test executes the `correct_bracketing` function with different inputs and confirms that the function returns the correct values.