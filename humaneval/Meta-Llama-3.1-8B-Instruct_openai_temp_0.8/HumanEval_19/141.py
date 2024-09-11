```python
from typing import Dict

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest

    Args:
    numbers (str): A space-delimited string of numbers

    Returns:
    str: The input string with numbers sorted from smallest to largest
    """
    
    # Create a dictionary to store the numbers and their corresponding integer values
    num_dict: Dict[str, int] = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Split the input string into a list of numbers
    numbers_list: List[str] = numbers.split()

    # Sort the list of numbers based on their values
    sorted_numbers: List[str] = sorted(numbers_list, key=lambda x: num_dict[x])

    # Join the sorted list of numbers into a string
    sorted_string: str =''.join(sorted_numbers)

    return sorted_string

# Example usage
print(sort_numbers('three one five'))  # Output: 'one three five'
print(sort_numbers('nine zero eight'))  # Output: 'zero nine eight'
```
This script first creates a dictionary to store the numbers and their corresponding integer values. It then splits the input string into a list of numbers, sorts the list based on the integer values, and joins the sorted list back into a string. The sorted string is then returned.