```python
def unique_digits(xs):
    """Return sorted list of elements in xs that contain no even digits."""
    return sorted([int for int in xs if not any(int % 2 == 0 for digit in str(int))])
```

This function `unique_digits(xs)` takes a list of integers `xs` as input and returns a sorted list of elements that contain no even digits. The function uses a list comprehension to iterate through each element in `xs`, checking if the string representation of the integer has any even digits. If it has any, it returns the element; otherwise, it returns an empty list. The function then returns a sorted list of the returned elements.

Here is an example usage of the function:
```python
print(unique_digits([15, 33, 1422, 1, 322]))
```
The output of this code is:
```
[1, 15, 33]
``` 

This corresponds to the first example in the original problem description.