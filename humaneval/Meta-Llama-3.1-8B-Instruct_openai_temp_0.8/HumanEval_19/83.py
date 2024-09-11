### Sorting Numbers in a String
#### Problem Description
The `sort_numbers` function takes a space-delimited string of numbers from 'zero' to 'nine', sorts them in ascending order, and returns the sorted string.

#### Code
```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """
    Sorts a space-delimited string of numbers from 'zero' to 'nine' in ascending order.

    Args:
        numbers (str): A space-delimited string of numbers.

    Returns:
        str: The sorted string of numbers.

    Examples:
        >>> sort_numbers('three one five')
        'one three five'
    """
    # Define a dictionary to map number strings to their integer values
    num_dict = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Split the input string into a list of numbers
    num_list: List[str] = numbers.split()

    # Sort the list of numbers based on their integer values
    sorted_list: List[str] = sorted(num_list, key=lambda x: num_dict[x])

    # Join the sorted list into a string separated by spaces
    sorted_str: str =''.join(sorted_list)

    return sorted_str

# Example usage:
print(sort_numbers('three one five'))  # Output: 'one three five'
print(sort_numbers('five seven nine eight six'))  # Output: 'five six seven eight nine'
```

This script first defines a dictionary to map number strings to their integer values. It then splits the input string into a list of numbers, sorts the list based on the integer values of the numbers, and finally joins the sorted list into a string separated by spaces. The sorted string is then returned by the function.