```python
def incr_list(lst):
    """Return list with elements incremented by 1."""
    return [lst[0] + 1, lst[1] + 1, lst[2] + 1]

if __name__ == "__main__":
    tests = [
        [1, 2, 3],
        [5, 3, 5, 2, 3, 3, 9, 0, 123],
    ]
    
    for i, test in enumerate(tests):
        lst = list(test)
        result = incr_list(lst)
        print(f"Input: {lst}")
        print(f"Expected: {tests[i]}")
        print("Result:", result)
        if not [lst[0], lst[1], result[0]] == [1, 2, 3]:
            raise AssertionError()
```