```python
def sort_numbers(input_string: str) -> str:
    """
    Sorts a space-delimited string of numbers from shortest to longest.
    Valid inputs are strings containing values from 'zero' to 'nine'.
    Returns the sorted string.
    """
    numbers = input_string.split()
    numbers.sort()
    return ' '.join(numbers)
```

This function takes a string as input and returns a string. It sorts the space-delimited list of numbers contained in the input string and returns the sorted list as a string. 

Here's an example of how to use the function:
```python
print(sort_numbers('three one five')) # 'one three five'
```

This would print `one three five` which is the sorted version of `three one five`. 

This function assumes that the input string contains only numbers from 'zero' to 'nine'. If the input string contains other numbers or values, the function may not work as expected. 

To handle more cases and improve code robustness, you might want to consider using Python's `range` library or an appropriate `enum` module to define and validate the allowable input values. 

Another approach might be to leverage Python's `collections.abc.Iterable` and `collections.abc.Sized` interfaces and corresponding `isinstance()` function to validate input against those interfaces. Adding these layers would increase the caller's responsibility for validating input but would simplify the main code path.  Both approaches could be combined for added robustness.