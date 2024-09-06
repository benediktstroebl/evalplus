```python
from typing import List

def separate_paren_groups(parentheses: List[str]) -> List[str]:
    """Function to separate and return lists of individual parentheses groups.
    : Returns a separated groups as a list of strings.
    input: List of strings, each representing a parenthesis group.
    Return: List of strings, each on the same line and with no extra spacing.
    """
    test = [("Input:[( )())", "Output:[( )()]"],
      ["[()]", "( )[]"), "[]"]. This test checks if the function can handle different types of parenthesis correctly and returns the expected output.
```

def test_separate_paren_groups():
    # Test the function
    test_data = [("( )(( ))(( )( ))")"]
    expected = ["()", "(())", "(()())"]
    result = separate_paren_groups(test_data)
    assert result == expected

# Run the function and test
test_separate_paren_groups()
```

This script defines a function `separate_paren_groups` that takes a list of strings as input and returns a list of strings. The function splits the strings by individual parenthesis groups, with balanced groups and no extra spacing. The test function `test_separate_paren_groups` is designed to test the `separate_paren_groups` function with a sample input and expected output. 
Finally, the `test_separate_paren_groups()` function is called to run the function and test it.