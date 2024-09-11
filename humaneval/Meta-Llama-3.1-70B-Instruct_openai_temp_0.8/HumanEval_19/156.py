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

    # Create a dictionary to map the word representation of numbers to their numerical values
    num_dict = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Split the input string into a list of words
    num_list: List[str] = numbers.split()

    # Sort the list of words based on their numerical values
    sorted_list: List[str] = sorted(num_list, key=lambda x: num_dict[x])

    # Join the sorted list of words back into a string
    sorted_string: str =''.join(sorted_list)

    return sorted_string


# Test the function
print(sort_numbers('three one five'))  # 'one three five'
print(sort_numbers('nine eight seven six five four three two one zero'))  
# 'zero one two three four five six seven eight nine'
print(sort_numbers('five four three two one'))  
# 'one two three four five'
```