```python
def unique_digits(xs):
    """Return sorted list of elements in xs with no even digit."""
    return sorted([int for int in xs if not any(int % 2 == 0 for digit in str(int))])
```

This approach iterates through each integer in the list `xs`, and checks if it contains any even digits when converted into a string. If there are no odd digits, it filters out the integer and eventually returns a sorted list of these filtered integers.

Here is the expected output for the test cases provided:
```python
>>> unique_digits([15, 33, 1422, 1])
[1, 15, 33]
>>> unique_digits([152, 323, 1422, 10])
[]
```

This approach has a time complexity of `O(n log n)`, where `n` is the length of the input list `xs`, due to the sorting operation. The space complexity is `O(n)`, as the code maintains an additional list to store the filtered integers.