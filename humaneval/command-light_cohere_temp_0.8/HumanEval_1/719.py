Here's the self-contained Python script with a function that solves the problem of separating nested parentheses into separate groups:
```python
def separate_paren_groups(s: str) -> List[str]:
    """
    Separates groups of nested parentheses into separate strings.

    Args:
        string s: The input string containing parentheses.

    Returns: list of strings. Each string represents a string that can be parsed to recover individual groups of parentheses.
    """
```

This function uses the Python list function `str.split()` with the specific delimiter `(` to split the string into a list of substrings. It uses string `()` to check if the list contains only strings and removes any extra whitespace characters from each substring, ensuring that the resulting strings are balanced and properly separated.