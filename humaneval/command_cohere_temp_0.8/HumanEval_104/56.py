```python
def unique_digits(xs):
    return sorted([x for x in xs if not any(int(y) % 2 == 0 for y in str(x))])
```
This function `unique_digits(xs)` takes a list of positive integers, `xs`, as input and returns a sorted list of all elements that do not have any even digits. The `not any()` function is used to efficiently check if there are any odd digits in the string representation of the number. This optimized checking allows the function to pass even larger tests, such as `unique_digits([152, 323, 1422, 10])`, which returns an empty list.