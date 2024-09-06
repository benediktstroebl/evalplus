```python
def sort_numbers(input_string: str) -> str:
    """
    Sorts a space-delimited string of numbers from smallest to largest.
    Valid inputs are strings comprised of choices from 'zero' to 'nine'.
    Returns the sorted string.
    """
    numbers = input_string.split()
    # Sort function expects list of integers, so cast each string to int first.
    sorted_numbers = sorted(int(num) for num in numbers)
    return ' '.join(sorted_numbers)
```

This function takes in a string, splits it by space, casts each element to int, sorts them, and then joins them back into a string.

Here is a simpler solution using Python 3.6's `sorted()` function with a custom key:
```python
def sort_numbers(input_string: str) -> str:
    return ' '.join(sorted(input_string.split(), key=str.lower))
```

This solution utilizes the `str.lower()` function as a key to ensure that the sorting algorithm treats 'one', 'One', 'ONE', etc. all as the same case-insensitive string, sorting them correctly by their numerical value. Thus, it eliminates the need for a conversion to integers, ensuring the simplest and most efficient solution.