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

    # Define a dictionary to map string numbers to their integer equivalents
    num_map = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Split the input string into a list of numbers
    nums: List[str] = numbers.split()

    # Convert the list of strings to a list of integers using the num_map dictionary
    nums_int: List[int] = [num_map[num] for num in nums]

    # Sort the list of integers
    nums_int.sort()

    # Convert the list of integers back to a list of strings using the num_map dictionary
    sorted_nums: List[str] = [list(num_map.keys())[list(num_map.values()).index(num)] for num in nums_int]

    # Join the sorted list of strings back into a string separated by spaces
    sorted_string: str =''.join(sorted_nums)

    return sorted_string


# Test the function
print(sort_numbers('three one five'))  # Outputs: 'one three five'
print(sort_numbers('nine eight seven'))  # Outputs:'seven eight nine'
print(sort_numbers('five four three'))  # Outputs: 'three four five'
```

This script defines a function `sort_numbers` that takes a space-delimited string of numbers from 'zero' to 'nine' and returns the string with numbers sorted from smallest to largest. It uses a dictionary `num_map` to map string numbers to their integer equivalents, and then uses list comprehensions and the `sort` method to sort the numbers. Finally, it joins the sorted list of strings back into a string separated by spaces.