```python
from typing import List, Dict

def sort_numbers(numbers: str) -> str:
    """
    This function takes a space-delimited string of numberals from 'zero' to 'nine',
    and returns the string with numbers sorted from smallest to largest.

    Args:
        numbers (str): A space-delimited string of numberals.

    Returns:
        str: The input string with numbers sorted from smallest to largest.
    """
    
    # Create a dictionary to map the numberals to their integer values
    num_dict: Dict[str, int] = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }
    
    # Split the input string into a list of numberals
    num_list: List[str] = numbers.split()
    
    # Use a lambda function as the key for the sort method, to sort the numberals based on their integer values
    num_list.sort(key=lambda x: num_dict[x])
    
    # Join the sorted list of numberals back into a string
    sorted_numbers: str =''.join(num_list)
    
    return sorted_numbers


# Example usage:
print(sort_numbers('three one five'))  # Outputs: 'one three five'
```
This script defines a function `sort_numbers` that takes a string of space-delimited numberals, sorts them in ascending order, and returns the sorted string. It uses a dictionary to map the numberals to their integer values, and the built-in `sort` method with a lambda function as the key to sort the numberals based on their integer values.