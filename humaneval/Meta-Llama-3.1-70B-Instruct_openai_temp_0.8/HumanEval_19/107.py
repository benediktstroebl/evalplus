```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """
    Sorts a space-delimited string of numbers from 'zero' to 'nine' in ascending order.

    Args:
    numbers (str): A space-delimited string of numbers.

    Returns:
    str: The input string with numbers sorted from smallest to largest.

    Example:
    >>> sort_numbers('three one five')
    'one three five'
    """

    # Define a dictionary to map number words to their integer values
    num_dict = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Split the input string into a list of number words
    num_list: List[str] = numbers.split()

    # Sort the list based on the integer values of the number words
    sorted_list = sorted(num_list, key=lambda x: num_dict[x])

    # Join the sorted list back into a string
    sorted_str =''.join(sorted_list)

    return sorted_str


# Test the function
print(sort_numbers('three one five'))  # Output: 'one three five'
```