```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """
    This function sorts a space-delimited string of numbers from 'zero' to 'nine' 
    in ascending order.

    Args:
        numbers (str): A space-delimited string of numbers from 'zero' to 'nine'.

    Returns:
        str: The sorted string.

    Example:
        >>> sort_numbers('three one five')
        'one three five'
    """
    # Split the input string into a list of numbers
    num_list: List[str] = numbers.split()

    # Create a dictionary to map number strings to their integer equivalents
    num_dict = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Convert the list to a list of integers
    num_list: List[int] = [num_dict[num] for num in num_list]

    # Sort the list of integers
    num_list.sort()

    # Convert the list of integers back to a list of strings
    num_list: List[str] = [list(num_dict.keys())[list(num_dict.values()).index(n)] for n in num_list]

    # Join the sorted list of strings into a single string
    sorted_str: str =''.join(num_list)

    return sorted_str


# Test the function
print(sort_numbers('three one five'))
print(sort_numbers('eight nine seven'))
print(sort_numbers('five six four'))
```