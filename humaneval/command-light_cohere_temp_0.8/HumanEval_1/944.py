```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    """
    Separates and returns list of non-empty strings representing each balanced group of parentheses.
    :param s: str
    :return: list(str)
    """
    # Initialize an empty list to store the result
    results = []

    # Iterate through each character in the string
    for char in s:
        # If it's a '(' or ')' char
        if char == '(' or char == ')':
            # Find the matching closing ')' and append it to the results list
            results.append(char)
        else:
            # If it's not '(', add it to the results list without splitting
            results.append(char)

    # Return the list of strings
    return results
``` 
This function, `separate_paren_groups`, takes a string `s` as input and returns a list of non-empty strings representing each balanced group of parentheses in `s`.  It uses a `for` loop to iterate through each character in the string and uses the `match` method to find the matching closing parenthesis, which is then added to the results list. 

The function does not use any built-in functions other than the `str` module and the `typing` module.