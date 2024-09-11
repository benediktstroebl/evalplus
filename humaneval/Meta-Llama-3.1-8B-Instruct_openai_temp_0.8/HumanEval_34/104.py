```markdown
### Unique Elements in a List
#### Problem Statement
Return sorted unique elements in a list.

#### Python Solution
```python
def unique(l: list):
    """
    Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    return sorted(set(l))

### Example Usage
if __name__ == "__main__":
    # Test the function
    print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```

### Explanation
The solution utilizes the built-in Python functions `set()` and `sorted()`.
- The `set()` function removes duplicates by converting the list into a set.
- The `sorted()` function sorts the resulting set in ascending order.
```