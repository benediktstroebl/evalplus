```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for segment in s.split():
        open, close = 0, 0
        for char in segment:
            if char == '(':
                open += 1
            else:
                close += 1
        result.append(open + close)
    return result
```
The function processes the input string in the following steps:
1. It splits the entire input string into different segments using space as a separator. Each segment represents a different group of parentheses. 
2. For each segment, it counts the number of open and close parentheses to calculate the depth of nesting. The deepest level of nesting is the sum of open and close parentheses.
3. Returns a list containing the deepest level of nesting for each group of parentheses. 

The unit tests are in the code to verify the functionality of the function. 

To run the tests, you can copy this code into a Python file (e.g., `parentheses.py`) and execute the command `python parentheses.py` in your terminal. Alternatively, you can execute the script directly if you have Python installed. This way, you can execute the script in a particular directory by typing `python parentheses.py` in the terminal in that directory. 

```python
import pytest

def test_parse_nested_parens():
    assert parse_nested_parens("(()()) ((())) () ((())()())") == [2, 3, 1, 3]
    assert parse_nested_parens("(()") == [1]
    assert parse_nested_parens("())") == [1]
    assert parse_nested_parens("(()()))") == [2, 1]
    assert parse_nested_parens("(((((()())")) == [3, 2, 1]
    assert parse_nested_parens("(()())") == [2]
    assert parse_nested_parens("()") == [0]
```