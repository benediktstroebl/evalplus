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
    # Create a dictionary to map number words to their numerical values
    num_map = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Split the input string into a list of number words
    num_list: List[str] = numbers.split()

    # Sort the list of number words based on their numerical values
    sorted_num_list = sorted(num_list, key=lambda x: num_map[x])

    # Join the sorted list of number words back into a string
    sorted_numbers =''.join(sorted_num_list)

    return sorted_numbers


# Example usage
print(sort_numbers('three one five'))  # Output: 'one three five'
print(sort_numbers('nine eight seven six five four three two one zero')) 
# Output: 'zero one two three four five six seven eight nine'
```

This script defines the `sort_numbers` function, which takes a space-delimited string of number words as input, sorts them in ascending order, and returns the sorted string. The function uses a dictionary to map number words to their numerical values and the `sorted` function with a custom sorting key to sort the list of number words. The sorted list is then joined back into a string and returned.