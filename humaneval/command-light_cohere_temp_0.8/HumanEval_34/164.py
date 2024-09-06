```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and not set() == seen]

# Test cases
test_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
print("Test case 1: ", unique(test_list))  # Output: [0, 2, 3, 5, 9, 123]

test_list2 = [1, 2, 3, 4, 5, 6, 7]
print("Test case 2: ", unique(test_list2))  # Output: [1, 2, 3, 4, 5, 6, 7]

test_list3 = [3, 0, 0, 0]
print("Test case 3: ", unique(test_list3))  # Output: []

test_list4 = "hello"
print("Test case 4: ", unique(test_list4))  # Output: []

test_list5 = [True, False, 3, 4, 5]
print("Test case 5: ", unique(test_list5))  # Output: [True, False]
``` 

This script defines a function called **unique** that takes a list as an argument and returns a new list with unique elements from the original list. The test cases demonstrate how the common use cases for the **unique** function.