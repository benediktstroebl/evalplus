```python
def separate_paren_groups(paren_string: str) -> List[str]:
    """Input is a string containing multiple groups of parentheses, each balanced with curly braces.

    Groups are separated into a balanced and properly formatted string with no extra spaces.
    Each group is separated with a single space.

    Returns: list of all groups.
    """
    string is split into individual groups of parentheses, balanced with curly braces.

    Test cases:
    - Basic parentheses
    - Pairs of brackets
    - Multi-level brackets
    - Curly braces
    - Everything else
    """
    return [p for p in paren_string.replace(). ... ]

# Test cases
tests = [
    '(', )',
    '()()', )',
    '(>)',
    '(()[])',
    '())',
    '()[][]',
    '(()())',
    '(>)()'
]

for test in tests:
    actual = separate_paren_groups(test)
    print(test, '->', actual)
```