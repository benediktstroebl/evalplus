```python
def sort_numbers(input_str: str) -> str:
    """
    Sorts a space-delimited string of numbers from smallest to largest.
    Valid choices are from 'zero' to 'nine'.
    """
    # Split the input string by space into a list of strings.
    # Using list comprehension, cast each string to int and sort them.
    # Join the sorted list with a space.
    return ' '.join(str(num) for num in sorted(map(int, input_str.split()), key=lambda x: x))
```