```python
from typing import Dict

# Define a dictionary to map number strings to their integer values
number_map: Dict[str, int] = {
    'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
    'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
}

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest

    Args:
        numbers (str): A space-delimited string of numberals.

    Returns:
        str: The string with numbers sorted from smallest to largest.
    """
    # Split the input string into a list of numbers
    num_list: List[str] = numbers.split()
    
    # Convert each number string to an integer using the number map
    num_list = [number_map[num] for num in num_list]
    
    # Sort the list of integers
    num_list.sort()
    
    # Convert each integer back to a string using the number map
    num_list = [list(number_map.keys())[list(number_map.values()).index(num)] for num in num_list]
    
    # Join the sorted list of strings back into a single string
    sorted_numbers: str =''.join(num_list)
    
    return sorted_numbers

# Example usage:
print(sort_numbers('three one five'))  # Output: 'one three five'
print(sort_numbers('nine seven three'))  # Output: 'three seven nine'
```
This script uses a dictionary to map each number string to its integer value, allowing for efficient lookup and sorting of the numbers. It then uses list comprehensions to convert the input string to a sorted list of integers, and finally converts the sorted list of integers back to a string using the number map.