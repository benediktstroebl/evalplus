```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """
    Sorts a space-delimited string of numbers in natural order.

    Args:
    numbers: A space-delimited string of numbers from 'zero' to 'nine'.

    Returns:
    A string with numbers sorted in natural order from smallest to largest.

    Example:
    >>> sort_numbers('three one five')
    'one three five'
    """

    # Split the input string into a list of numbers
    num_list: List[str] = numbers.split()

    # Define a custom sorting key to sort the numbers in natural order
    def natural_key(num: str) -> str:
        """
        Custom sorting key to sort numbers in natural order.

        Args:
        num: A string of a number from 'zero' to 'nine'.

        Returns:
        A string with the number's value in the natural ordering.
        """
        ordinal: int = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9}.get(num)
        return str(ordinal)

    # Sort the list of numbers using the custom sorting key
    sorted_num_list: List[str] = sorted(num_list, key=natural_key)

    # Join the sorted list of numbers back into a string
    sorted_numbers: str =''.join(sorted_num_list)

    return sorted_numbers


# Example usage:
print(sort_numbers('three one five'))  # Output: 'one three five'
```