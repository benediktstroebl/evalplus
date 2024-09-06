```python
def sort_numbers(input_str: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest.
    """
    numbers = input_str.split()
    sorted_numbers = ' '.join(sorted(numbers))
    return sorted_numbers
```

This Python script defines a function called `sort_numbers` that takes in a string parameter input_str, which is expected to be a space-delimited string of single numbers from 'zero' to 'nine'. These valid numbers are sorted in ascending order and returned as a string using the split and join methods.