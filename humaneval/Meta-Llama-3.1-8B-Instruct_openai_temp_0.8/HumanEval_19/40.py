```python
from collections import OrderedDict

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest

    Args:
    numbers (str): A space-delimited string of numberals.

    Returns:
    str: The string with numbers sorted from smallest to largest.
    """
    # Create a dictionary to map string numbers to their corresponding integer values
    number_dict = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,'six': 6, 
                  'seven': 7, 'eight': 8, 'nine': 9}

    # Split the input string into a list of numbers
    num_list = numbers.split()

    # Sort the list of numbers based on their integer values
    sorted_num_list = sorted(num_list, key=lambda x: number_dict[x])

    # Use OrderedDict to remove duplicates while preserving order
    sorted_num_list = list(OrderedDict.fromkeys(sorted_num_list))

    # Join the sorted list of numbers back into a string
    sorted_string =''.join(sorted_num_list)

    return sorted_string

# Test the function
print(sort_numbers('three one five'))
print(sort_numbers('nine eight seven six five four three two one'))
print(sort_numbers('zero one two three four five six seven eight nine'))
```

This script defines a function `sort_numbers` that takes a space-delimited string of numbers as input, sorts them based on their corresponding integer values, and returns the sorted string. The function uses a dictionary to map string numbers to their integer values and the `sorted` function with a lambda function as the `key` argument to sort the list of numbers. Finally, the script includes test cases to demonstrate the function's correctness.