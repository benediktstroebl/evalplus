```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """
    Sorts a space-delimited string of number words from smallest to largest.

    Args:
        numbers (str): A string of number words separated by spaces.

    Returns:
        str: The input string with the number words sorted from smallest to largest.
    """
    
    # Define a dictionary to map number words to their integer values
    num_dict = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }
    
    # Split the input string into a list of number words
    num_list = numbers.split()
    
    # Check if all number words are valid
    for num in num_list:
        if num not in num_dict:
            raise ValueError(f"Invalid number word: {num}")
    
    # Sort the list of number words based on their integer values
    num_list.sort(key=lambda x: num_dict[x])
    
    # Join the sorted list of number words into a string separated by spaces
    sorted_nums =''.join(num_list)
    
    return sorted_nums

# Example usage:
print(sort_numbers('three one five'))  # Output: 'one three five'
```