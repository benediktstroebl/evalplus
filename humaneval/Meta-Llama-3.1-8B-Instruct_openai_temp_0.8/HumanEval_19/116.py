```python
from typing import List, Dict

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest

    Args:
    numbers (str): A space-delimited string of numberals.

    Returns:
    str: The sorted string of numberals.
    """
    # Create a dictionary to map string numbers to integers
    num_dict: Dict[str, int] = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Split the input string into a list of numbers
    num_list: List[str] = numbers.split()

    # Sort the list of numbers based on their integer values
    sorted_num_list: List[str] = sorted(num_list, key=lambda x: num_dict[x])

    # Join the sorted list into a string separated by spaces
    sorted_num_str: str =''.join(sorted_num_list)

    return sorted_num_str

# Test the function
print(sort_numbers('three one five'))  # Expected output: 'one three five'
print(sort_numbers('five four three'))  # Expected output: 'three four five'
print(sort_numbers('nine eight seven six five four three two one'))  # Expected output: 'one two three four five six seven eight nine'
```
This script defines a function `sort_numbers` that takes a space-delimited string of numbers as input, sorts them based on their integer values, and returns the sorted string. It uses a dictionary to map string numbers to integers, and the built-in `sorted` function with a lambda function as the `key` argument to sort the list of numbers. The result is then joined back into a string separated by spaces.