```python
def sort_numbers(input_string: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest.
    """
    numbers = input_string.split()
    numbers.sort()
    return ' '.join(numbers)
```
The function takes an input string, splits it by spaces, sorts the list of numbers, and then joins them back with spaces to produce the output string. This algorithm solves the problem in a straightforward manner.