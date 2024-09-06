```python
def max_element(lst):
    """Return maximum element in the list"""
    return max(lst)

# Test case 1
my_list = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
print(max_element(my_list))  # Output: 123

# Test case 2
my_list = [5, 3, -5, 2, -3]
print(max_element(my_list))  # Output: 5

# Test case 3
my_list = [-5, -3, 3, 2, -10, 0, 1]
print(max_element(my_list))  # Output: 3
```
The function `max_element` in the above code snippet efficiently returns the maximum element in the input list using the `max()` function. The test cases demonstrate the-specific scenarios, passing various lists and obtaining the expected output. 

To fully solve this problem and ensure the correctness of your implementation, it is important to include test cases that cover different scenarios, such as empty lists, lists with only one element, lists with duplicate elements, and lists with negative values.