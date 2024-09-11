```python
# Define a dictionary to map number words to their integer values
number_mapping = {
    'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
    'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
}

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest

    Args:
        numbers (str): A space-delimited string of numbers.

    Returns:
        str: The string with numbers sorted from smallest to largest.
    """
    # Split the input string into a list of number words
    num_list = numbers.split()

    # Use the dictionary to map number words to their integer values
    num_list = [number_mapping[word] for word in num_list]

    # Sort the list of numbers
    num_list.sort()

    # Map the numbers back to their word representations
    num_list = [list(number_mapping.keys())[list(number_mapping.values()).index(num)] for num in num_list]

    # Join the sorted list of numbers back into a string
    sorted_numbers =''.join(num_list)

    return sorted_numbers

# Test the function
print(sort_numbers('three one five'))  # Output: 'one three five'
```

This script defines a function `sort_numbers` that takes a space-delimited string of numbers as input, sorts them from smallest to largest, and returns the sorted string. The function uses a dictionary to map number words to their integer values, sorts the numbers using the `sort` method, and then maps the numbers back to their word representations before returning the sorted string. The script also includes a test case to verify that the function works correctly.