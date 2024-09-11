```python
from typing import List


def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numbers from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    # Create a dictionary to map string numbers to integers
    num_map = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Split the input string into a list of numbers
    numbers_list: List[str] = numbers.split()

    # Sort the list of numbers based on their integer equivalents
    numbers_list.sort(key=lambda x: num_map[x])

    # Join the sorted list back into a string
    sorted_numbers: str =''.join(numbers_list)

    return sorted_numbers


# Test the function
print(sort_numbers('three one five'))  # Output: one three five
print(sort_numbers('eight five six'))  # Output: five six eight
print(sort_numbers('nine four'))  # Output: four nine
```

This script defines the `sort_numbers` function to take a space-delimited string of numbers, sort them based on their integer equivalents, and return the sorted string. The function uses a dictionary to map string numbers to integers, splits the input string into a list, sorts the list, and then joins it back into a string. The script also includes test cases to demonstrate the function's behavior.