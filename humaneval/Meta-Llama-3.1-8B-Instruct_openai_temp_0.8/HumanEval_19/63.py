```python
from typing import List


def sort_numbers(numbers: str) -> str:
    """
    Sorts a string of space-delimited numbers from 'zero' to 'nine' in ascending order.

    Args:
        numbers (str): A space-delimited string of numberals from 'zero' to 'nine'.

    Returns:
        str: The input string with numbers sorted from smallest to largest.

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
    sorted_num_list: List[str] = sorted(num_list, key=lambda x: num_dict[x])

    # Join the sorted list back into a string
    sorted_numbers: str =''.join(sorted_num_list)

    return sorted_numbers


# Test the function
print(sort_numbers('three one five'))  # Output: 'one three five'
print(sort_numbers('eight nine seven'))  # Output:'seven eight nine'
print(sort_numbers('zero five one'))  # Output: 'one five zero'
```

This script uses a dictionary to map number strings to their integer values, allowing for efficient sorting based on these integer values. The `sorted` function with a custom key function is used to sort the list of numbers. Finally, the sorted list is joined back into a string and returned as the result.