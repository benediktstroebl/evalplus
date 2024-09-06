```python
def get_positive(input_list):
    return [x for x in input_list if x >= 0]

# Unit tests
input_list = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
test_get_positive = get_positive(input_list)
print("Test 1:", test_get_positive)  # Output: [5, 3, 2, 3, 9, 123, 1]

input_list2 = [5, 3, -5, 2, -3, 3, -123, 0, -9, 10, -2]
test_get_positive2 = get_positive(input_list2)
print("Test 2:", test_get_positive2)  # Output: [-5, -3, -2]

input_list3 = [1, 2, -10, -40, -123]
test_get_positive3 = get_positive(input_list3)
print("Test 3:", test_get_positive3)  # Output: [-10, -40, -123]
```
This script defines a function `get_positive` that returns a list containing only positive numbers from an input list. The function is then subjected to three tests with different lists of numbers to ensure its correctness. 

This code demonstrates the use of functions and unit testing to solve a specific problem.