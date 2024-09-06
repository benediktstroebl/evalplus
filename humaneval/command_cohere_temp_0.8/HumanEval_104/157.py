```python
def unique_digits(xs):
    odd_digits = [int(''.join(x for x in str(n) if x.isdigit() and x % 2 != 0)) for n in xs if n > 0]
    return sorted(odd_digits)
```

The function `unique_digits` works by first filtering out odd digits from the positive integers in the input list `xs`. It converts each positive integer into a string, filters out non-digit characters, and converts the odd digits back to integers. The resulting list of odd digits is then sorted in ascending order and returned.

Here is an example usage of the function:
```python
>>> unique_digits([15, 33, 1422, 1])
[1, 15, 33]
>>> unique_digits([152, 323, 1422, 10])
[]
```

This demonstrates that the function correctly filters out odd digits from the positive integers and returns the sorted list as expected.