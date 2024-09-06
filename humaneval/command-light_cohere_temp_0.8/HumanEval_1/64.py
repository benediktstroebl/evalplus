```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    """
    Function to separate and return groups of parentheses.
    Each group of parentheses should be balanced and no nested within each other.
    Returns a regular expression is used to split the string based on balanced parentheses.
    """: a list comprehension is used to extract the matches.
    """
    final list will just string with the parentheses balanced and spaces removed.
    """: Test code
    The function with a test string and compares the output with the expected result."""

def test_separate_paren_groups():
    assert separate_paren_groups('( ) (( )) (( )( ))')' == ['()', '(())', '(()())'])', ensuring balanced and correct grouping of parentheses.

test_separate_paren_groups()  # Test function with test string

# Call the function to run the test
separate_paren_groups('( ) (( )) (( )( ))')')  # Run the function
```