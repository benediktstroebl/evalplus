```python
def unique_digits(xs):
    """Return sorted list of elements in xs with no even digits."""
    return sorted(x for x in xs if not any(int(d) % 2 == 0 for d in str(x)))
```

The script employs a list comprehension, filtered entries that do not have any even digits in their integer representations. It then employs the `sorted()` function to organize the filtered entries in an ascending sequence.

Here is an example of how to employ the function unique_digits() to solve the problem:
```python
unique_digits([15, 33, 1422, 1]) # Output: [1, 15, 33]
```
```python
unique_digits([152, 323, 1422, 10]) # Output: []
```

The function unique_digits() effectively handles the task at hand, providing the desired output. The method is implemented in a efficient manner, utilizing a single pass to assess each entry in the input list.