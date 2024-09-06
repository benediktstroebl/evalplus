```python
def sort_numbers(input_string: str) -> str:
    """
    Sorts a space-delimited string of numbers from shortest to longest.
    Valid inputs are strings containing digits from 0 to 9.
    Returns the sorted string.
    """
    numbers = input_string.split()
    numbers.sort()
    return ' '.join(numbers)
```

This code defines a Python function called `sort_numbers` that takes a string as its input. This string contains space-separated numbers from 0 to 9. The function splits this input string into a list of numbers, sorts this list in ascending order, and then joins the sorted numbers back into a string. Finally, it returns this sorted string.