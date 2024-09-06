```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    # Initialize the output list
    results = []
    
    # Iterate through each group of parentheses
    for group in s.group(s):
        # Parse each group of parentheses
        results.append(parse_group(group))
    
    return results
# Test cases
def test_parse_nested_parens():
    # Test one string with nested parentheses
    test_string = "(()()) ((())) () ((()))"
    
    # Call the parse_nested_parens function
    results = parse_nested_parens(test_string)
    
    # Assert that the output is correct
    assert len(results) == 4
    assert results[0] == 2
    assert results[1] == 3
    assert results[2] == 1
    assert results[3] == 3
``` 
The provided Python code defines a function `parse_nested_parens` that takes a string of nested parentheses as input and returns a list of corresponding integer levels of nesting. 

The `test_parse_nested_parens` function serves as a test case, providing a sample string to be processed by the `parse_nested_parens` function.