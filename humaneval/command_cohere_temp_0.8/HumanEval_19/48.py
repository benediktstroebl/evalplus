```python
def sort_numbers(input_string: str) -> str:
    """
    Sorts a space-delimited string of numbers from shortest to longest.
    Valid input includes integers from 0 to 9.
    """
    # Split the input string by space into a list of strings.
    # Using list comprehension, convert each string to an integer.
    # Using `sorted` function, sort the list of integers.
    # Join the sorted list of integers back into a string.
    return ' '.join(sorted(map(int, input_string.split())))
```