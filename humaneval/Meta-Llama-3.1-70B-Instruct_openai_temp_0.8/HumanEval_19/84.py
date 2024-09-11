```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """
    This function takes a space-delimited string of numberals from 'zero' to 'nine', 
    and returns the string with numbers sorted from smallest to largest.
    
    Args:
        numbers (str): A string containing space-delimited numberals.
    
    Returns:
        str: The input string with numbers sorted from smallest to largest.
    """

    # Define a dictionary to map number words to their integer values
    num_map = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Split the input string into a list of number words
    num_words = numbers.split()

    # Sort the list of number words based on their integer values
    sorted_num_words = sorted(num_words, key=lambda x: num_map[x])

    # Join the sorted list of number words back into a string
    sorted_numbers =''.join(sorted_num_words)

    return sorted_numbers


# Test the function
print(sort_numbers('three one five'))  # Output: 'one three five'
print(sort_numbers('eight four two'))  # Output: 'two four eight'
print(sort_numbers('nine zero one'))   # Output: 'zero one nine'
```