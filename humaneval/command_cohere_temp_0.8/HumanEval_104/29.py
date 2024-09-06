Here is a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
def unique_digits(xs):
    """Return sorted list of elements in xs with no even digits."""
    return sorted(x for x in xs if not any(int(d) % 2 == 0 for d in str(x)))
```
The unique_digits function employs a list comprehension to iterate through each element in the input list xs. It filters elements using a generator expression, checking if any digit in the string representation of the element is even. The resulting list of elements is then sorted in ascending order using the sorted function and returned.

To ensure the function is self-contained and doesn't rely on external resources or modules, it uses native Python functionalities and does not import any additional libraries.