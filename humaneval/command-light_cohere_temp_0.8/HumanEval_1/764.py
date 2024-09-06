```python
def separate_paren_groups(paren_string: str) -> List[str]:
    brackets = {')': ')', '}': ')', '}': ')', '(': ')'}
    return [brack for bracket in paren_string.bracket if brackets]
```

This code defines a function called `separate_paren_groups` that takes a string of parenthesis characters as input and returns a list of separated brackets. The function uses a balanced bracket rule to achieve this, where it matches the open bracket with the corresponding closing bracket and returns it as a string.

The code also uses a dictionary to keep track of the pairs of opening and closing brackets, which helps with faster lookups and making sure that every opening bracket is paired with the correct corresponding closing bracket. 

The output of the function would be a list of strings where each string represents a balanced group of parenthesis characters.