```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """
    Sorts a string of space-delimited number words from 'zero' to 'nine' in ascending order.

    Args:
    numbers (str): A space-delimited string of number words.

    Returns:
    str: The input string with the number words sorted from smallest to largest.
    """
    # Define a dictionary to map number words to their corresponding integer values
    num_dict = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Split the input string into a list of number words
    num_list = numbers.split()

    # Sort the list of number words based on their corresponding integer values
    sorted_num_list = sorted(num_list, key=lambda x: num_dict[x])

    # Join the sorted list of number words back into a string
    sorted_numbers =''.join(sorted_num_list)

    return sorted_numbers

# Example usage:
print(sort_numbers('three one five'))  # Output: 'one three five'
```

In this script, we define a dictionary `num_dict` to map number words to their corresponding integer values. We split the input string into a list of number words, sort the list based on the integer values using the `sorted()` function, and then join the sorted list back into a string using the `join()` method. The resulting string is returned as the output.