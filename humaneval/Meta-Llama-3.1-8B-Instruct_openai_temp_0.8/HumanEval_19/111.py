### Python Script to Sort Numbers in a String

```python
from typing import List
import re

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
    # Define a dictionary to map the number strings to integers
    num_dict = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 
                'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9}

    # Use regular expression to extract numbers from the input string
    nums = re.findall(r'\w+', numbers)

    # Sort the numbers based on their integer values
    sorted_nums = sorted(nums, key=lambda x: num_dict[x])

    # Join the sorted numbers back into a string
    sorted_str =''.join(sorted_nums)

    return sorted_str

# Example usage:
print(sort_numbers('three one five'))  # Output: 'one three five'
print(sort_numbers('eight two five nine'))  # Output: 'two five eight nine'
```

This script defines a function `sort_numbers` that takes a string of space-delimited numbers as input. It first uses a dictionary to map the number strings to integers. Then it uses regular expression to extract the numbers from the input string. The numbers are sorted based on their integer values and joined back into a string, which is returned as the result. The script also includes example usage to demonstrate its functionality.