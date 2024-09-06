```python
def unique_digits(xs):
    return sorted([x for x in xs if not any(int(y) % 2 == 0 for y in str(x))])
```
This Python script defines a function `unique_digits` that takes a list of positive integers as input (`xs`). It filters this list using a list comprehension, omitting entries with even digits. The resulting list is then sorted in ascending order and returned.

To check the correctness of the solution, the following tests are performed:
```python
# Test a list with single item
>>> unique_digits([15])
[15]

# Test a list with multiple items
>>> unique_digits([15, 33, 1422, 1])
[1, 15, 33]

# Test a list with items containing only even digits
>>> unique_digits([152, 322, 1422, 10])
[]
```

The script successfully passes these tests, confirming that it satisfies the problem statement's requirements.