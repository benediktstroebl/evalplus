```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    # Create a dictionary to map number words to their integer equivalents
    number_map = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Split the input string into a list of number words
    number_words = numbers.split()

    # Sort the list of number words based on their integer equivalents
    sorted_number_words = sorted(number_words, key=lambda x: number_map[x])

    # Join the sorted list of number words back into a string
    sorted_numbers =''.join(sorted_number_words)

    return sorted_numbers


# Test the function
print(sort_numbers('three one five'))  # Expected output: 'one three five'
print(sort_numbers('nine eight seven six five four three two one zero'))  
# Expected output: 'zero one two three four five six seven eight nine'
```