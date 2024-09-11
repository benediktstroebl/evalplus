```python
from typing import List, Dict

def sort_numbers(numbers: str) -> str:
    """
    Sorts a space-delimited string of numberals from 'zero' to 'nine' in ascending order.

    Args:
        numbers (str): A space-delimited string of numberals.

    Returns:
        str: The input string with numbers sorted from smallest to largest.

    Example:
        >>> sort_numbers('three one five')
        'one three five'
    """
    # Define a dictionary to map number words to their numerical values
    num_dict: Dict[str, int] = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Split the input string into a list of number words
    num_list: List[str] = numbers.split()

    # Sort the list of number words based on their numerical values
    sorted_num_list: List[str] = sorted(num_list, key=lambda x: num_dict[x])

    # Join the sorted list of number words back into a string
    sorted_numbers: str =''.join(sorted_num_list)

    return sorted_numbers


# Test the function
print(sort_numbers('three one five'))  # Output: 'one three five'
```

This script defines a function `sort_numbers` that takes a space-delimited string of numberals as input and returns the string with numbers sorted from smallest to largest. The function uses a dictionary to map number words to their numerical values, sorts the list of number words based on these values, and then joins the sorted list back into a string. The script also includes a test case to demonstrate the function's usage.