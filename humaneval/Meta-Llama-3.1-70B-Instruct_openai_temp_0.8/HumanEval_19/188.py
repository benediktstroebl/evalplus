```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    """
    
    # Create a dictionary mapping the word representation of numbers to their integer values
    num_dict = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }
    
    # Split the input string into a list of words
    num_list = numbers.split()
    
    # Check if all words in the list are valid numbers
    if not all(word in num_dict for word in num_list):
        raise ValueError("Invalid input. All words must be valid numbers.")
    
    # Sort the list of words based on their integer values
    sorted_list = sorted(num_list, key=lambda x: num_dict[x])
    
    # Join the sorted list back into a string
    sorted_numbers =''.join(sorted_list)
    
    return sorted_numbers

# Test the function
print(sort_numbers('three one five'))  # Output: 'one three five'
```

This script defines a function `sort_numbers` that takes a string of space-delimited numbers as input, sorts them in ascending order, and returns the sorted string. The function uses a dictionary to map the word representation of numbers to their integer values, allowing it to sort the numbers correctly. It also checks if all words in the input string are valid numbers, raising an error if any invalid words are found.