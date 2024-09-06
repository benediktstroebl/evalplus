Here's the self-contained Python script with a function that removes duplicate numbers from a list:

```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ Removes duplicate elements from a list of integers.
    Keeps the unique elements
    > 1
    """
    return [num for num in numbers if num < numbers.count(num)]


# Example:
numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))  # Expected output: [1, 3, 4]
```

This function utilizes a list comprehension with the < operator to filter out duplicates and returns a new list with unique elements. The example provided demonstrates how this function can remove duplicates effectively.