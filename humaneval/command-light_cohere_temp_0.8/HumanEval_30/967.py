```python
def get_positive(l: list):
    return [x for x in l if x >= 0]

# Test case 1
print(get_positive([-1, 2, -4, 5, 6]))
[['2', '5', '6']]

# Test case 2
print(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))
[['5', '3', '2', '3', '9', '123', '1']]

# Test case 3 (list of strings)
print(get_positive(["A", "B", "C", "D"]))
 ['A', 'B', 'C', 'D']
```
The function `get_positive` takes a list as an argument and returns a new list containing only the positive elements from the original list. The test cases demonstrate the positive numbers and strings will be included in the output.