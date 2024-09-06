```python
def max_element(lst):
    return lst[-1] if len(lst) == 1 else max(lst)

# Test cases
test_max_element = [
    [1, 2, 3],
    [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10],
    [5, -5, 3, -20, 2]
]

for test in test_max_element:
    assert max_element(test) == max(test)
```
The function max_element takes a list as input and returns the maximum element in the list. It uses the max() function to find the maximum value, which is the last element in the list. This is a way to solve the problem in a self-contained manner.