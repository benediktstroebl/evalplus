```python
import typing

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', and 'nine'.
    Return the string with numbers sorted from smallest to largest.
    >>> sort_numbers('three one five')
    'one three five'
    """
    return typing.String(sorted(numbers.split(), key=[str]))

if __name__ == "__main__":
    numbers = """
    three one five
    six two seven
    eight nine
    """
    print(sort_numbers(numbers))
``` 
Do you have a self-contained function to sort a list of numbers in Markdown format?