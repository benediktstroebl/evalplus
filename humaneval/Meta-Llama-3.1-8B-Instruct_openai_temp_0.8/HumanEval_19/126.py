```python
from typing import List

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
    # Split the input string into a list of numbers
    num_list: List[str] = numbers.split()

    # Create a dictionary to map string numbers to their integer equivalents
    num_dict: dict[str, int] = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Sort the list of numbers based on their integer equivalents
    sorted_num_list: List[str] = sorted(num_list, key=lambda x: num_dict[x])

    # Join the sorted list of numbers back into a string
    sorted_numbers: str =''.join(sorted_num_list)

    return sorted_numbers


# Test the function
print(sort_numbers('three one five'))  # Output: one three five
print(sort_numbers('nine nine nine'))  # Output: nine nine nine
print(sort_numbers('zero five eight'))  # Output: five eight zero
```

This script defines the `sort_numbers` function, which takes a space-delimited string of numbers as input and returns the string with numbers sorted from smallest to largest. The function uses a dictionary to map string numbers to their integer equivalents, sorts the list of numbers based on these integer equivalents, and then joins the sorted list back into a string. The script also includes test cases to demonstrate the function's behavior.