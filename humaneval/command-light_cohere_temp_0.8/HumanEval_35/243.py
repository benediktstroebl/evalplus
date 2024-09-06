```python
def max_element(lst):
    if not_positive(lst):
        return float('-inf')
    return max(lst)

def not_positive(lst):
    return all(x > 0 for x in lst)

# Test the max_element function
test_max_element = []
test_max_element.add(range(0, 4))
test_max_element.add([range(5, -2, -3))
test_max_element.add([range(-5, -10, -3))
test_max_element.add(range(-10, 0))

for test in test_max_element:
    assert max_element(test) == max(test), "Test 1 failed"

print("All tests passed!")
```