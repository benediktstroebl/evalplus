### Sorting Numbers in a String
#### Problem Description

Given a space-delimited string of numberals from 'zero' to 'nine', sort the numbers in ascending order.

#### Solution

```python
from typing import Dict

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    
    >>> sort_numbers('three one five')
    'one three five'
    """
    
    # Define a dictionary mapping string numbers to their integer value
    num_dict: Dict[str, int] = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }
    
    # Split the input string into a list of numbers
    num_list: List[str] = numbers.split()
    
    # Sort the list of numbers using a custom key function
    sorted_num_list: List[str] = sorted(num_list, key=lambda x: num_dict[x])
    
    # Join the sorted list back into a string
    sorted_string: str =''.join(sorted_num_list)
    
    return sorted_string

# Example usage
print(sort_numbers('three one five'))  # Output: 'one three five'
```

This script uses a dictionary to map string numbers to their integer value, allowing for easy sorting. The `sorted` function is used with a custom key function to sort the list of numbers based on their integer value. Finally, the sorted list is joined back into a string using the `join` method.