Here is a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
def unique_digits(xs):
    return sorted([x for x in xs if not any(int(y) % 2 == 0 for y in str(x))])
```

The function unique_digits(xs) takes a list of positive integers called xs and returns a sorted list of all elements that do not contain any even digits. The function checks if any digit of the string representation of the integer is even, using the expression int(y) % 2 == 0 for each digit y of the element x. The list comprehension returns a list of integers if such elements are found, which is then sorted in increasing order and returned.

You can test this function with the following commands:
```python
>>> unique_digits([15, 33, 1422, 1])
[1, 15, 33]
>>> unique_digits([152, 323, 1422, 10])
[]
```

These tests follow the ones provided in the original problem. Let me know if you would like me to explain any part of the code further!