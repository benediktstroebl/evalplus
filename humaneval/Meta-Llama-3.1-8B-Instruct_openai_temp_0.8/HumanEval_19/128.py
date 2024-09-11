### Sorting Numbers in a String

Below is a Python script that implements a function to sort numbers in a string in ascending order.

```python
from typing import List

# Dictionary mapping number strings to integers
num_string_to_int = {
    'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
    'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
}

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numbers from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest.
    
    Args:
        numbers (str): A space-delimited string of numbers.

    Returns:
        str: The input string with numbers sorted in ascending order.
    """
    # Split the input string into a list of numbers
    num_list = numbers.split()
    
    # Convert each number string to an integer using the dictionary
    num_list = [num_string_to_int[num] for num in num_list]
    
    # Sort the list of integers
    num_list.sort()
    
    # Convert each integer back to a number string
    num_list = [list(num_string_to_int.keys())[list(num_string_to_int.values()).index(num)] for num in num_list]
    
    # Join the list of number strings back into a string separated by spaces
    sorted_numbers =''.join(num_list)
    
    return sorted_numbers

# Example usage:
print(sort_numbers('three one five'))  # Output: 'one three five'
print(sort_numbers('nine eight seven six five four three two one'))  # Output: 'one two three four five six seven eight nine'
```

This script defines a function called `sort_numbers` that takes a string of space-delimited numbers as input. It first splits the input string into a list of numbers, then converts each number string to an integer using a dictionary. The list of integers is then sorted in ascending order using the built-in `sort` method. Finally, each integer is converted back to a number string, and the list of number strings is joined back into a string separated by spaces. The sorted string is then returned by the function.