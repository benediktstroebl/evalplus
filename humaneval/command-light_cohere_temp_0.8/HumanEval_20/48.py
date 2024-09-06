```python
from typing import List

def find_closest_elements(numbers: List[float]):
    """
    From a supplied list of numbers (of length at least 2), select and return two that are the closest to each other and return them in order (smaller number, larger number).
    Returns a tuple of the two closest numbers.

    # Sort the Due list in descending order
    numbers.sort( ascending=False, key=numbers)
    numbers.sort()

   (ascending=False)
    # Select first two numbers in sorted list
    first, second = numbers[:2]
    # Check if first number is less than second number
    if first < second:
        # Return both numbers in order of smaller to larger
        return (first, second)
    elif first == second:
        # Return both numbers in order of equal to each other
        return (first, second)
    else:
        # Return only the larger number
        return (second, first)

```

This function is designed to find the closest pair of elements in the supplied list of numbers. It does this following:
- Sorts the list of numbers in descending order based on their values using the sort() function.
- Selects the first two numbers from the sorted list.
- If two numbers are stored in first and second variables.
- It is then checked if the first number is less than the second number. If this is the case, the function returns a tuple containing both numbers in the order of smaller to larger number.
- If other case, the function returns a tuple containing only the second number.

It is worth noting that the function uses the sort() function with ascending=False to sort the list in descending order. The function also uses the list comprehension to select the first two numbers from the sorted list.