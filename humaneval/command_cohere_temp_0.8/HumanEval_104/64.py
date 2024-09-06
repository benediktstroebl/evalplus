```python
def unique_digits(xs):
    return sorted([x for x in xs if not any(int(y) % 2 == 0 for y in str(x))])
```
This Python script provides a function `unique_digits(xs)` that takes in a list of positive integers, `xs`, and returns a sorted list of all elements that do not contain any even digits. The function filters the list using a list comprehension, checking if any digit in each element's conversion to a string is even, and then sorts the result.  This solves the problem statement in a self-contained manner, as it does not rely on any external modules or assumptions beyond those stated in the prompt.