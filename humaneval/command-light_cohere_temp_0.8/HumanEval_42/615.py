```python
def incr_list(lst):
    """Return list with elements incremented by 1."""
    lst[::] = 1 + lst[:]
    return lst

if __name__ == "__main__":
    tests = [
        [1, 2, 3],
        [5, 3, 5, 2, 3, 3, 9, 0, 123],
        [(), 1, 2, 3, 4, 5, 6],
        [10, 2, 3, 4, 5, 6, 7]
    ]

    for test in tests:
        got = incr_list(test)
        expected = test
        print(f"Test 1: {got}, {expected}")
        assert got == expected, "Test 1 failed"
        print(" --- ")

    print("All tests passed")
```