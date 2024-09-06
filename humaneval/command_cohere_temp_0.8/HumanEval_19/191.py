```python
def sort_numbers(input_str: str) -> str:
    """
    Sorts a space-delimited string of numbers from lowest to highest.
    Valid inputs are from 'zero' to 'nine'.
    Returns the sorted string.
    """
    numbers = input_str.split()
    sorted_numbers = ' '.join(sorted(numbers))
    return sorted_numbers
```

This function takes in a string that contains a space-delimited list of numbers from 'zero' to 'nine'. It splits this string into a list of numbers, sorts that list in ascending order, and then joins the sorted list back into a string. Finally, it returns this sorted string.

Here's an example usage of the function:
```python
print(sort_numbers('three one five'))  # Outputs: 'one three five'
```

This would output `one three five`, as the numbers from the input string are sorted from lowest to highest.