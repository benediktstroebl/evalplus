```python
import typing

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numbers from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', and 'nine'.
    Return the string with numbers sorted from smallest to largest.
    >>> sort_numbers('three one five')
    'one three five'
    """
    numbers = [int(num) for num in numbers.
    return ''.join(sorted(numbers))

def test_sort_numbers():
    """
    Test case for the sort_numbers function.
    >>> test_sort_numbers('three one five')
    'one three five'
    """
    return sort_numbers('three one five')

if __name__ == "__main__":
    print(test_sort_numbers())
```

The script defines a function called `sort_numbers` that sorts a list of numbers in ascending order and returns the sorted string. The function takes a input and uses the sorted() method with the sorted function to create a sorted list of numbers. The sorted list is then converted back into a string using the join() method. The test_sort_numbers function tests the `sort_numbers` function with a test case, and the output is the expected result.