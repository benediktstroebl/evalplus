```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    result = [0] * (n + 1)
    result[0] = l[0]
    for i in range(1, n+1):
        result[i] = l[i - 1] + 1
    return result

# Test the function with a range of inputs
test_cases = [
    [1, 2, 3],
    [5, 3, 5, 2, 3, 3, 9, 0, 123],
    [1, 2, 7, 3, 6, 5, 4, 4, 2],
    [100, 80, 60, 50, 40, 30]
]

for i, test in enumerate(test_cases):
    actual = incr_list(test)
    expected = test
    print(f"Test {i+1}: {actual} vs. expected: {expected}")
    print()
```

The function `incr_list` takes a list as input and returns a new list with elements incremented by 1. The function uses an iterative approach with a loop that runs from index 1 to the length of the list. The increment is set to 1, and the original list elements are referenced within the loop. The resulting list contains the elements from the original list incremented by 1.