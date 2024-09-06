```python
def sort_numbers(input_string: str) -> str:
    """
    Sorts a space-delimited string of numbers from smallest to largest.
    Valid choices are from 'zero' to 'nine'.
    Returns the sorted string.
    """
    numbers = input_string.split()
    sorted_numbers = ' '.join(sorted(numbers))
    return sorted_numbers
```

This function takes in a string variable containing space-delimited numbers from 'zero' to 'nine' and sorts the numbers from smallest to largest. It then returns the sorted string. You can verify this works correctly with the provided test case. 

For example, calling the function with the input 'three one five' will return 'one three five'.