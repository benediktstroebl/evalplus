```python
import typing


def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numbers from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Returns the string with numbers sorted from smallest to largest
    """
    numbers = [int(num) for num in numbers.
    return ' '.join(sorted(numbers))


def test_sort_numbers():
    """
    Test case: 'three one five'
    Expected output: 'one three five'
    """
    return sort_numbers('three one five')


if __name__ == "__main__":
    numbers = "three one two seven eight five six four".split()
    print(test_sort_numbers())
```