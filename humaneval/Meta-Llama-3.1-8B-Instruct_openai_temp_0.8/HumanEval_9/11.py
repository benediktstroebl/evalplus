### Rolling Maximum Element in a Sequence

Here's a Python script that uses a list comprehension to generate a list of rolling maximum elements in a sequence.

```markdown
### rolling_max.py

```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    Generate a list of rolling maximum element found until given moment in the sequence.

    Args:
    numbers (List[int]): A list of integers.

    Returns:
    List[int]: A list of rolling maximum elements.

    Example:
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    return [max(numbers[:i+1]) for i in range(len(numbers))]

# Test the function
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))
```

### Output

When you run this script, it will print the list of rolling maximum elements for the given sequence `[1, 2, 3, 2, 3, 4, 2]`.

### Explanation

*   We define the `rolling_max` function that takes a list of integers as input.
*   Inside the function, we use a list comprehension to create a new list where each element is the maximum of all elements up to that point in the input list.
*   We achieve this by using `max(numbers[:i+1])`, which returns the maximum of the slice of the input list up to the current index `i`.
*   The function then returns this new list of rolling maximum elements.
*   Finally, we test the function with the example sequence and print the result.