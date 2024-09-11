```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """
    Sorts a space-delimited string of numbers from 'zero' to 'nine' in ascending order.

    Args:
        numbers (str): A space-delimited string of numbers.

    Returns:
        str: The input string with numbers sorted from smallest to largest.
    """
    
    # Define a dictionary to map number words to their integer values
    num_map = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }
    
    # Split the input string into a list of number words
    num_list = numbers.split()
    
    # Use the dictionary to map number words to their integer values, sort the list, and then map back to number words
    sorted_num_list = [num for _, num in sorted(zip(map(num_map.get, num_list), num_list))]
    
    # Join the sorted list back into a string
    sorted_numbers =''.join(sorted_num_list)
    
    return sorted_numbers


# Example usage:
print(sort_numbers('three one five'))  # Output: 'one three five'
```

This script defines a function `sort_numbers` that takes a space-delimited string of number words, sorts them in ascending order, and returns the sorted string. It uses a dictionary to map number words to their integer values, allowing for easy sorting. The example usage demonstrates how to use the function with a sample input string.