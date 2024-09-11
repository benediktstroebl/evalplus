### Python Script to Sort Numbers in a String
```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """
    Sorts a space-delimited string of numbers from 'zero' to 'nine' in ascending order.

    Args:
        numbers (str): A space-delimited string of numbers from 'zero' to 'nine'.

    Returns:
        str: The sorted string with numbers from smallest to largest.
    """
    # Define a dictionary to map numbers to their corresponding integer values
    num_dict = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }
    
    # Split the input string into a list of numbers
    num_list: List[str] = numbers.split()
    
    # Sort the list of numbers based on their integer values
    sorted_num_list: List[str] = sorted(num_list, key=lambda x: num_dict[x])
    
    # Join the sorted list of numbers back into a string
    sorted_str: str =''.join(sorted_num_list)
    
    return sorted_str

# Example usage
print(sort_numbers('three one five'))  # Output: 'one three five'
```
This script defines a function `sort_numbers` that takes a space-delimited string of numbers as input, sorts them in ascending order, and returns the sorted string. It uses a dictionary to map numbers to their corresponding integer values and the `sorted` function with a custom sorting key to achieve this.