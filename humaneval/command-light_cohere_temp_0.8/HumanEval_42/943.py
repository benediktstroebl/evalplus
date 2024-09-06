```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    new_list = [x + 1 for x in l]
    return new_list

# Test case 1
test_case1 = [[1, 2, 3]]
test_result1 = incr_list(test_case1)
print("Test case 1: ", end="")
print(test_result1)

# Test case 2
test_case2 = [5, 3, 5, 2, 3, 3, 9, 0, 123]
test_result2 = incr_list(test_case2)
print("\nTest case 2: ", end="")
print(test_result2)

# Test case 3
test_case3 = [100, 200, 300]
test_result3 = incr_list(test_case3)
print("\nTest case 3: ", end="")
print(test_result3)
```
This script defines a function incr_list that takes a list l as an argument and returns a new list with elements incremented by 1. 

The test cases are created as lists with specific values, and the incr_list function is called with each test case. The expected output for each test case will be the new list with elements incremented by 1.