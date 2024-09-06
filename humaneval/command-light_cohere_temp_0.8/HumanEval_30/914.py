```python
def get_positive(lst):
    return [num for num in lst if num >= 0]

# Test the function with various input lists
test_get_positive = []
test_get_positive.add([list([-1, 2, -4, 5, 6]))
test_get_positive.add([list([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))

# Validate the function output with assert
for test_list in test_get_positive:
    assert len(get_positive(test_list)) == len(test_list)
    print("Test passed")
```