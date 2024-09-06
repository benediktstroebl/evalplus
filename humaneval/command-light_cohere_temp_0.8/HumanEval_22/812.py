```python
from typing import List

def filter_integers(values:
    """
    return [x for x in values if type(x) == int]
):
```

This function takes a list of values as an argument and returns a new list containing only the integers from the input. It does this using a list comprehension and type checking to achieve this.

Let's break down the code further:
- `from typing import List`: This line is importing the List type from the `typing` module.
- `def filter_integers(values:`: This line defines the function named `filter_integers` that takes a single argument `values`.
- Inside the function:
    - `[x for x in values if type(x) == int]`: This line is using a list comprehension to create a new list. The list comprehension iterates over each element in the `values` list and checks if the element's type is `int`. Then, it adds the element to the new list.
- The return statement is returning the new list created.