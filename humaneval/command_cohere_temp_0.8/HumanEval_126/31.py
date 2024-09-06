```python
def is_sorted(lst):
    dups = {}
    for n in lst:
        if n in dups:
            dups[n] += 1
        else:
            dups[n] = 1
    for n, count in dups.items():
        if count > 1:
            return False
    return all(n <= m for n, m in zip(lst, lst[1:]))
```

The function employs a dictionary (`dups`) to track occurrences of each number in the list `lst`, initially assuming all elements are unique. It then iterates through this dictionary, identifying numbers that appear more than once and returning `False` if any count exceeds unity. Lastly, it compares each element to its subsequent ones through a zipper and returns `True` only if all comparisons yield `n <= m`. 

Here is a test suite that can be used to validate the function:
```python
def test_is_sorted():
    # Test cases from the problem statement
    assert is_sorted([5])
    assert is_sorted([1, 2, 3, 4, 5])
    assert not is_sorted([1, 3, 2, 4, 5])
    assert is_sorted([1, 2, 3, 4, 5, 6])
    assert is_sorted([1, 2, 3, 4, 5, 6, 7])
    assert not is_sorted([1, 3, 2, 4, 5, 6, 7])
    assert is_sorted([1, 2, 2, 3, 3, 4])
    assert not is_sorted([1, 2, 2, 2, 3, 4])

    # Edge cases
    assert is_sorted([])
    assert is_sorted([1])
    assert is_sorted([1, 2])
    assert is_sorted([0, 0, 0, 0, 0])

    # Negative numbers
    assert not is_sorted([1, -2, 3, -4, 5])

    # Mixed types
    assert not is_sorted([1, 2, '3', 4, 5])

    # Larger list
    assert is_sorted([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

test_is_sorted()
```

This test suite includes the examples from the problem statement and additional edge cases to ensure the function remains effective across diverse inputs. 

*Note*: This script assumes that the `is_sorted` function has already been defined in the current environment. If it has not, you can add the function by pasting the first code snippet into your Python environment.