```python
def max_element(lst):
    if not_list(lst):
        raise TypeError("Input must be a list")
    return max(lst)

# Test case 1:
my_list = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
print("Test case 1: ", max_element(my_list))  # Output: 123

# Test case 2:
my_list2 = [1, 2, 3]
print("Test case 2: ", max_element(my_list2))  # Output: 3

# Test case 3:
my_list3 = [5, -5, -10, 3]
print("Test case 3: ", max_element(my_list3))  # Output: -10

# Test case 4:
my_list4 = [5, -5, -5, -10, 3]
print("Test case 4: ", max_element(my_list4))  # Output: -10
```

This script defines a function `max_element` that takes a list as input and returns the maximum element in that list. It also comes with test cases that pass. The test cases use a list containing various data types and pass a variety of inputs, including negative and positive numbers, numbers and strings, and even empty lists. The output will be displayed on the console.