```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    """
    # Define a dictionary to map number words to their integer values
    num_dict = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Split the input string into a list of number words
    num_words = numbers.split()

    # Sort the list of number words based on their integer values
    sorted_num_words = sorted(num_words, key=lambda x: num_dict[x])

    # Join the sorted list of number words into a string
    sorted_numbers =''.join(sorted_num_words)

    return sorted_numbers


# Example usage:
print(sort_numbers('three one five'))  # Output: 'one three five'
```