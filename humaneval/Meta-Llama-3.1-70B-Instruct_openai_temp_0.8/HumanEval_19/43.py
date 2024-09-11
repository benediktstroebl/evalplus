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
    # Define a dictionary to map the number words to their corresponding integer values
    number_mapping = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Split the input string into a list of number words
    number_words = numbers.split()

    # Sort the number words based on their corresponding integer values
    sorted_number_words = sorted(number_words, key=lambda x: number_mapping[x])

    # Join the sorted number words back into a string separated by spaces
    sorted_numbers =''.join(sorted_number_words)

    return sorted_numbers


# Example usage:
print(sort_numbers('three one five'))  # Output: 'one three five'
print(sort_numbers('nine eight seven six five four three two one zero'))  
# Output: 'zero one two three four five six seven eight nine'
```

This script first defines a dictionary `number_mapping` to map the number words to their corresponding integer values. It then splits the input string into a list of number words, sorts them based on their corresponding integer values using the `sorted` function with a `lambda` function as the `key` argument, and finally joins the sorted number words back into a string separated by spaces.