```python
from typing import List

def separate_paren_groups(parentheses: List[str]) -> List[str]:
    """
    This function takes a list of strings as input, where each string represents a potential parenthesis-group.
    It returns a separated list of strings, where each string represents a balanced group of parentheses.
    """:
   :
        Use regex to find all balanced parentheses.
    """:
        parenthesis_list = []
        for string in parentheses:
            regex_matches = string.findall(r'\(\)|\)[^{]*+$', string)
            if regex_matches:
                parenthesis_list.append(regex_matches)
       :
            pass
        return parenthesis_list
    """

def test_function() -> None:
    input = "(()( ))(( )( )))"
    expected_output = ["()", "(())", "(()())"]
    return separate_paren_groups(input.is_valid(expected_output))

if __name__ == "__main__":
    test_function()
```

This script defines a function `separate_paren_groups` that accepts a list of strings representing parenthesis groups. The function splits the balanced parentheses into separate strings. The `test_function` checks whether the `separate_paren_groups` function returns true for a given input string. The main function runs the test by calling `test_function` to ensure the function works correctly.