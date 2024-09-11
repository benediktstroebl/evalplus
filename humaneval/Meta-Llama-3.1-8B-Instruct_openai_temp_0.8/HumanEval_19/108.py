```python
def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numbers from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest

    Args:
        numbers (str): A space-delimited string of numbers.

    Returns:
        str: The input string with numbers sorted from smallest to largest.
    """
    # Split the input string into a list of numbers
    num_list = numbers.split()

    # Create a dictionary to map string numbers to integers
    num_dict = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Sort the list of numbers based on the integer values
    sorted_num_list = sorted(num_list, key=lambda x: num_dict[x])

    # Join the sorted list into a string and return it
    return''.join(sorted_num_list)


# Test the function
print(sort_numbers('three one five'))  # Output: 'one three five'
print(sort_numbers('nine zero eight'))  # Output: 'zero nine eight'
```

This Python script first splits the input string into a list of numbers. It then creates a dictionary to map each string number to its corresponding integer value. The list of numbers is sorted based on these integer values, and finally, the sorted list is joined back into a string and returned.