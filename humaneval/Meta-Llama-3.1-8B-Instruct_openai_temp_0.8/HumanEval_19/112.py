```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numbers from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest

    Args:
        numbers (str): A space-delimited string of numberals

    Returns:
        str: The string with numbers sorted from smallest to largest
    """
    # Define a dictionary to map string numbers to their integer values
    number_map = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Split the input string into a list of numbers
    num_list: List[str] = numbers.split()

    # Sort the list of numbers based on their integer values
    num_list.sort(key=lambda x: number_map[x])

    # Join the sorted list back into a string separated by spaces
    sorted_nums: str =''.join(num_list)

    return sorted_nums

# Test the function
print(sort_numbers('three one five'))  # Output: one three five
print(sort_numbers('nine seven five'))  # Output: five seven nine
print(sort_numbers('eight five seven six four three two one zero'))  # Output: zero one two three four five six seven eight
```

This Python script defines a function `sort_numbers` that takes a space-delimited string of numbers from 'zero' to 'nine' as input, sorts them from smallest to largest based on their integer values, and returns the sorted string. The function uses a dictionary to map string numbers to their integer values and employs the `sort` method with a custom sorting key to achieve the desired result.