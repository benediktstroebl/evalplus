```python
def sort_numbers(input_str: str) -> str:
    """
    Sorts a space-delimited string of numbers from smallest to largest.
    Valid inputs are strings composed of choices from 'zero' to 'nine'.
    Returns the sorted string.
    """
    # Split the input string into a list of numbers
    numbers = [char for char in input_str if char in 'zero one two three four five six seven eight nine']
    # Sort the list of numbers
    sorted_numbers = ' '.join(sorted(numbers))
    # Return the sorted string
    return sorted_numbers
```

This function takes a string as input and returns a string of sorted numbers that are space-delimited in the original input. It ensures that only valid numbers from 'zero' to 'nine' are sorted, and these are the only characters that will be handled correctly in this function. Any other characters will be ignored.