```python
from typing import List, Dict

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numbers from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest

    Args:
        numbers (str): A space-delimited string of numbers

    Returns:
        str: The input string with numbers sorted from smallest to largest
    """
    # Create a dictionary to map number names to their integer values
    num_dict: Dict[str, int] = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Split the input string into a list of numbers
    number_list: List[str] = numbers.split()

    # Sort the list of numbers based on their integer values
    sorted_list: List[str] = sorted(number_list, key=lambda x: num_dict[x])

    # Join the sorted list back into a string separated by spaces
    sorted_string: str =''.join(sorted_list)

    return sorted_string


# Test the function
print(sort_numbers('three one five'))  # Output: one three five
print(sort_numbers('five seven nine'))  # Output: five seven nine
```

This script defines the `sort_numbers` function which takes a string of space-delimited numbers, sorts them based on their integer values, and returns the sorted string. The function uses a dictionary to map number names to their integer values, allowing it to efficiently sort the numbers. The script also includes example test cases to demonstrate the function's behavior.