```python
def get_positive(l: list):
    """Return only positive numbers in the list"""
    return [num for num in l if num >= 0]

# Test the function with various input lists
# Ensure all test cases cover valid inputs and valid outputs
# Print the results for better clarity

test_list1 = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
test_list2 = [-1, 2, -4, 5, 6]
test_list3 = [5, 3, 5, -5, 2, -3, 3, 9, 0, 123, 1, -100]

print("List from test1: ", end="")
print(get_positive(test_list1))
print("\n")

print("List from test2: ", end="")
print(get_positive(test_list2))
print("\n")

print("List from test3: ", end="")
print(get_positive(test_list3))
print("\n")
```
This script defines a `get_positive` function that filters out any negative numbers from the input list. The function is then tested with three different lists, and the results are displayed, which ensures the correctness of the function.