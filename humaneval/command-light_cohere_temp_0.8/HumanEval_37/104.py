```python
def sort_even(lst):
    return sorted(lst, key=lambda x: x if x % 2 == 0 else x + 1)

# Test cases
tests = {
    "input": [1, 2, 3],
    "output": [1, 2, 3],
    "expected": [1, 2, 3]
}

# Execute the function and test
test_results = sort_even(**tests["input"])
print("Test Results:", test_results)
```