Here's the self-contained Python function that sorts a string of numbers from 'zero' to 'nine':
```python
def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numbers from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    
    # Verify that all numbers from zero to nine are valid
    if 'zero' not in numbers. + ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']:
        raise ValueError("The input contains an invalid number.")

    # Use a list comprehension to sort the numbers
    numbers = [int(num) for num in numbers.

    # Convert the done list to a string, with spaces between the numbers
    return ' '.join(numbers)
```
The function takes a string of numbers, separated by spaces, and returns a string where the numbers are sorted from smallest to largest. The function also raises a ValueError if an invalid number is found in the input string.