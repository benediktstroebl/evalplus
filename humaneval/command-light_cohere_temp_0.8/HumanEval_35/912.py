```python
def max_element(lst):
    if not_positive(lst):
        return float('-inf')
    return max(lst)

def not_positive(lst):
    return all(x > 0 for x in lst)

# Test function to check max element in positive list
def test_positive():
    return max_element([1, 2, 3]) == 3

# Test function to check max element in negative list
def test_negative():
    return max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == 123
```
The test functions test the max_element function with the appropriate inputs and verify if the output matches the expected result. The max_element function utilizes the simple approach to solve this problem and returns the maximum element in the list. The function first checks if the list contains only positive numbers and returns negative infinity in this case. If the list contains positive numbers, it returns the maximum element as the final result.