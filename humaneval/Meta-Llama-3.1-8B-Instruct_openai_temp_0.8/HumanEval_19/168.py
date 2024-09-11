```python
from typing import Dict

# Create a dictionary mapping string numbers to integer values
number_map: Dict[str, int] = {
    'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
    'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
}

def sort_numbers(numbers: str) -> str:
    """
    Sorts a space-delimited string of numberals from 'zero' to 'nine'.

    Args:
    numbers (str): A space-delimited string of numberals from 'zero' to 'nine'.

    Returns:
    str: The string with numbers sorted from smallest to largest.
    """
    
    # Split the input string into a list of string numbers
    num_list: List[str] = numbers.split()
    
    # Sort the list of string numbers using a custom key function
    # The key function maps each string number to its corresponding integer value
    sorted_num_list: List[str] = sorted(num_list, key=lambda x: number_map[x])
    
    # Join the sorted list of string numbers into a single string separated by spaces
    sorted_numbers: str =''.join(sorted_num_list)
    
    return sorted_numbers

# Example usage:
print(sort_numbers('three one five'))  # Output: 'one three five'
print(sort_numbers('nine eight seven six five four three two one zero'))  # Output: 'zero one two three four five six seven eight nine'
```

This script first defines a dictionary `number_map` that maps each string number to its corresponding integer value. It then defines the `sort_numbers` function, which splits the input string into a list of string numbers, sorts this list using a custom key function, and finally joins the sorted list into a single string separated by spaces. The example usage demonstrates how to use this function.