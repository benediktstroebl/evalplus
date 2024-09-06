Here's a Python script that includes a function to solve the given problem:
```python
def add_elements(arr, k):
    sum_two_digits = sum(el for el in arr[:k] if len(str(el)) <= 2)
    return sum_two_digits
    # The line above uses a generator expression to sum only the elements that have at most two digits.
```

This script defines a function `add_elements(arr, k)` that takes an array `arr` and an integer `k` as input, and calculates the sum of elements in `arr` that have at most two digits when converted to a string.

The generator expression `el for el in arr[:k] if len(str(el)) <= 2` creates a generator that iterates over the first `k` elements of `arr`, and yields each element `el` if the length of its string representation `len(str(el))` is at most 2. The sum of these elements is then calculated using the `sum()` function.