```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """
    This function takes a string of space-delimited number words, 
    and returns the string with numbers sorted from smallest to largest.

    Args:
        numbers (str): A string containing space-delimited number words.

    Returns:
        str: The input string with number words sorted from smallest to largest.
    """
    
    # Define a dictionary to map number words to their integer values
    num_dict = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }
    
    # Split the input string into a list of number words
    num_list = numbers.split()
    
    # Check if all number words are valid
    if not all(num in num_dict for num in num_list):
        raise ValueError("Invalid number word in input string.")
    
    # Sort the number words based on their integer values
    sorted_list = sorted(num_list, key=lambda x: num_dict[x])
    
    # Join the sorted number words back into a string
    sorted_string =''.join(sorted_list)
    
    return sorted_string

# Test the function
print(sort_numbers('three one five'))  # Output: 'one three five'
```