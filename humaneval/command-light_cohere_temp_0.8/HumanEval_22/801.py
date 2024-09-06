```python
def filter_integers(values):
    return [x for x in values if type(x) == int]

# Test cases
values_test = [
    ['a', 3.14, 5],
    [1, 2, 3, 'abc', {}, []]
)

assert filter_integers(values_test) == [5, 1, 2, 3]

# Description of the solution: The function filters out non-integer values from the input list using list comprehension.
```