```python
def get_positive(lst):
    return [num for num in lst if num >= 0]

# Test the function with a list of numbers
test_list = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
actual = get_positive(test_list)
print("Actual:", actual)

# Test the function with a list of strings
test_strings = ["a", "b", "A", "B"]
actual_ = get_positive(test_strings)
print("Actual:", actual)

# Test the function with an empty list
test_empty = []
actual_ = get_positive(test_empty)
print("Actual:", actual)
```
This script defines a function `get_positive` that accepts a list as an argument. The feature takes each list and returns a new list containing only the positive numbers from the original list. It is then a function using a variety of test cases to guarantee that it functions appropriately and prints the results.