```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    l = [i + 1 for i in l]
    assert(all([i >= 1 for i in l]) and all([i <= n for i in l]))
    return l
# Test cases
test_cases = [
    [1, 2, 3],
    [5, 3, 5, 2, 3, 3, 9, 0, 123],
    [6, 7, 8, 9]
]

for test_case in test_cases:
    print(f"Test case: {test_case[0]}")
    print("Increment:", end='' * 30)
    for l in test_case:
        print(' -> ', l)
    incr_list(l)
    print("\n")
```  This Python script defines a function `incr_list` that increments all elements in a list by 1. It uses a string formatting and list comprehension to efficiently build the new list. The function also includes assertion tests to ensure the correctness of its implementation.