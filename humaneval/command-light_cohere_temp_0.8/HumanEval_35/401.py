```python
def max_element(lst):
    if not_numbers(lst):
        return float('-inf')
    return max(lst)

def not_numbers(lst):
    return any(map(lambda x: x != 0, lst))

# Test cases
test_max_element = []
test_max_element.add([list([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))
test_max_element.add([list([None, 'abc', 123, [1, 2, 3], [4, 5, 6]]))
test_max_element.add([list([[], [1, 2, 3], [5, 6], [7, 8]])
test_max_element.add([list([1, 2, 3, [4, 5], [6], [7, 8], [9]]))

# Run the tests using the built function
for test in test_max_element:
    assert max_element(test) == max(test)
```