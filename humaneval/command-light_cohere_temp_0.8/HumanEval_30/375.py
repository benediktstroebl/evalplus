```python
def get_positive(lst):
    return [x for x in lst if x >= 0]

# Test the function with different lists of numbers
tests = [ [-1, 2, -4, 5, 6], [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10], [1, 2, 3, 7, -8, 9 ]]

for test_lst in tests:
    actual = get_positive(test_lst)
    expected = test_lst
    print(f"Test passed: got {actual}, expected {expected}")
```