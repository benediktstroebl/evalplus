```python
def separate_paren_groups(parentheses: str) -> List[str]:  # Python function to separate groups of parentheses into individual strings
    return [p for p in parentheses if '(' not in p and ')' not in p]  # Filter out any characters that are not parentheses or closing parentheses
    
def test_parentheses_separation(test_str):  # Test string to check the function
    return separate_paren_groups(test_str) == ['(', ')', '()]  # Test cases are true
```  The provided code defines a function `separate_paren_groups` that takes a string of parentheses as input and returns a list of individual strings that can be extracted from the given string by separating the parenthesis groups. The `test_parentheses_separation` function is designed to test the `separate_paren_groups` function with a given test string.  The purpose of this function is to remove all characters except parentheses from the input string.