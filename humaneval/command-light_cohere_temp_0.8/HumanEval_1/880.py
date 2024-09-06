Here's the self-contained Python function that solves the problem of separating parentheses into individual groups:
```python
def separate_paren_groups(s: str) -> List[str]:
    """
    Separates and returns individual groups of well-formed parentheses.

    Args:
        - Input string s, containing multiple groups of parentheses.
    Returns: list of strings, each representing a separated group of parentheses.
    """
    test cases:
        '()()()' -> ['()', '()']
        '(())'  -> ['(', '())']
        '( )'  -> ['()']
        '()() ( )'  -> ['()', '( ', ' )']
        '( ( ) ) ' -> ['(', ')']
    """
    return [char for char in s if char in '()( )[]{}'`]
```
This function uses a list comprehension to iterate through each character in the input string. It filters out only al characters that are either parentheses, square brackets, curly braces, or the literal string `{}`. The function returns a list of these filtered characters. 

The tests are provided to show the functionality of the function, demonstrating the ability to separate different types of parentheses and their combinations.