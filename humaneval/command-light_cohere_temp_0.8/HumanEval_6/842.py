```python
from typing import List
def parse_nested_parens(parent_string: str) -> List[int]:
    """
    This function is designed to accept a string of parenthesis groups, 
    representing nested parentheses, and return the deepest level of nesting for each group.
    Inputs are string to parse.
    : returns a format is a list of deepest nesting levels.
    """ 
    :param parent_string: the string to parse.
    :return: a list of deepest nesting levels
    """
    return [match.group().index for match in re.match.group in 
        re.parent_string.findall('('(', ', ')')). }

def test_parse_nested_parens():
    """
    This function runs tests on the parse_nested_parens function. 
    """
    test_cases for the parse_nested_parens function
    """
    # Test case 1:
    test_str = "(()()) ((())) () ((())())"
    result = parse_nested_parens(test_str)
    assert result == [2, 3, 1, 3]
    # Test case 2:
    test_str = "((((())))))"
    result = parse_nested_parens(test_str)
    assert result == [4]
    # Test case 3:
    test_str = "()()()()()"
    result = parse_nested_parens(test_str)
    assert result == []
    # Test case 4:
    test_str = "((()))"
    result = parse_nested_parens(test_str)
    assert result == []
    # Test case 5:
    test_str = "() () () ()()"
    result = parse_nested_parens(test_str)
    assert result == []
    # Test case 6:
    test_str = "(())"
    result = parse_nested_parens(test_str)
    assert result == []
```