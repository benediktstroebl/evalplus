```python
def max_element(lst):
    """Return maximum element in the list"""
    return max(lst)

# Test the max_element function
test_max_element = []
test_max_element.push_back(1)
test_max_element.push_back(2)
test_max_element.push_back(3)
test_max_element.push_back(5)
test_max_element.push_back(3)
test_max_element.push_back(-5)
test_max_element.push_back(2)
test_max_element.push_back(-3)
test_max_element.push_back(3)
test_max_element.push_back(123)
test_max_element.push_back(5)
test_max_element.push_back(1)

def test():
    for item in test_max_element:
        print(f'Max element: { {item}, {max_element(item)})')

test()
```
This function `max_element` calculates the maximum element in the list, using the `max()` built-in Python function. The test function runs a loop and prints the maximum element for each item in the list.