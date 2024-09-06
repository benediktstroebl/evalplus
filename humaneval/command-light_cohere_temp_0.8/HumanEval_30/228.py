```python
def get_positive(l: list):
    """Return only positive numbers in the list"""
    return [num for num in l if num >= 0]

# Test the function with a sample input
input_list = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
result = get_positive(input_list)
print(result)

# Test the function with another list with negative numbers
test_list = [-1, 2, -4, 5, 6]
result2 = get_positive(test_list)
print(result2)
```
The function get_positive takes a list as input and returns a new list containing only the positive numbers from the original input list. The function is tested with two sample lists, and the output is printed for verification.