Here's a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
def same_chars(s0, s1):
    return sorted(s0) == sorted(s1)
```
The function definition `def same_chars(s0, s1):` takes two strings as arguments and returns a boolean indicating whether the two strings have the same characters when sorted. The function achieves this by using the `sorted()` function to sort the characters in the strings and comparing the sorted versions of both strings for equality. Consequently, it returns `True` if the sorted versions are identical, indicating that the strings have the same characters in any order, and `False` otherwise.

This approach allows the function to accommodate cases where the characters within the strings are identical, irrespective of their positions.