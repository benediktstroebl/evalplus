```python
def unique_digits(xs):
    """Return sorted list of elements in xs that have no even digits."""
    return sorted([int for int in xs if not any(int % 2 == 0 for digit in str(int))])
```

This function `unique_digits(xs)` takes a list of integers `xs` as input and returns a sorted list of elements that contain no even digits. The function uses a list comprehension that iterates through each element in `xs`, checking if an integer has any even digits in its decimal representation. The notation `int for int in xs` is shorthand for `list(map(int, xs))`, which internally converts the list of strings (`xs`) into a list of integers. The `not any()` function is a shortcut for `iter(<condition>) and not any(map(<condition>, iter(<sequence>)))`, so inside the list comprehension, it checks if any of the digits in the decimal representation of the integer is even (`int % 2 == 0 for digit in str(int)`). 

The function returns a sorted list of integers that do not have any even digits for elements where the condition is met.

This solution has a time complexity of O(n log n) due to the sorting and a space complexity of O(n) to store the output list.