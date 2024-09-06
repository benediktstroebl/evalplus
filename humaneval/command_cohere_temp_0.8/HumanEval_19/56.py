```python
def sort_numbers(input_string: str) -> str:
    """
    Sorts a space-delimited string of numbers from smallest to largest.
    Valid inputs are strings comprised of choices from 'zero' to 'nine'.
    Returns the sorted string.
    """
    # Split the input string into a list of strings
    # Assuming the input string contains only digits,
    # cast each element to integers for comparison
    numbers = [int(x) for x in input_string.split()]
    # Sort the list of integers
    sorted_nums = sorted(numbers)
    # Join the sorted list into a string
    return ' '.join(str(x) for x in sorted_nums)
```