```python
def max_element(lst):
    return max(lst)

# Test cases
tests = [
    [list([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])], None)
    ([], None)
    ([1, 2, 3, 4, 5])
    ([10, 100, 200])
    ([10, -10])
    ([1, -1, -10, 10])

for lst, expected in tests:
    print(f"Test {lst}, expected {expected}")
    actual = max_element(lst)
    print(f"Actual: {actual}, Expected: {expected})")
    if actual != expected:
        print("Failed")
    else:
        print("Passed")
```