Here is a self-contained Python script that defines a function named `separate_paren_groups`, which takes a string of parentheses as input and returns a list of separated groups:
```python
from typing import List
def separate_paren_groups(parentheses: str) -> List[str]:
    """Separate groups of parentheses into separate strings.
    > Returns balanced (each open brace is properly closed) and not nested within each other.
    > Returns any spaces in the string to maintain readability and avoid confusion.
    """ The balanced (each open brace is properly closed) and not nested within each other
    other.
    Return a list of those separate strings.
    """
    balanced and the return the list of separated strings.
    """
balanced (balanced parentheses are crucial for correct evaluation and interpretation).
    """:
    return [parent for i, p in enumerate(parentheses.replace('('): p + (') :: max(parentheses[i + 1 :]))]
```
This function uses a list comprehension to iterate through each group of parentheses in the input string. The `parentheses` variable stores the list of open parentheses '('), and the `p` variable keeps track of the closing parenthesis ')' that has just been added to the current group. The `max(parentheses[i + 1 :])` part ensures that the closing parenthesis for the current group is added only once. The function then returns a list of separated strings, which are the balanced groups of parentheses.