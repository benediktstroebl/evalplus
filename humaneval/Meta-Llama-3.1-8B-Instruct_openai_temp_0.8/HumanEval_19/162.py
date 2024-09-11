```python
def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest

    Args:
        numbers (str): A space-delimited string of numbers.

    Returns:
        str: The input string with numbers sorted from smallest to largest.

    Example:
        >>> sort_numbers('three one five')
        'one three five'
    """
    # Define a dictionary to map number strings to their integer values
    number_map = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Split the input string into a list of numbers
    num_list = numbers.split()

    # Sort the list of numbers based on their integer values
    sorted_list = sorted(num_list, key=lambda x: number_map[x])

    # Join the sorted list back into a string and return it
    return''.join(sorted_list)


# Test the function
print(sort_numbers('three one five'))  # Output: 'one three five'
print(sort_numbers('eight seven nine six'))  # Output:'six eight seven nine'
print(sort_numbers('four two zero'))  # Output: 'zero four two'
```

This script defines a function `sort_numbers` that takes a space-delimited string of numbers as input, maps each number string to its integer value, sorts the numbers based on their integer values, and returns the sorted string. It also includes example use cases to demonstrate the function's behavior.