Here's a self-contained Python function that filters out integers from a list of various types:
```python
def filter_integers(values):
    return [int(x) for x in values if type(x) == int]

# Test cases
values_test_case1 = ['a', 3.14, 5]
values_test_case2 = [1, 2, 3, 'abc', {}, []]

print("Test case 1:")
print(filter_integers(values_test_case1))

print("\n")

print("Test case 2:")
print(filter_integers(values_test_case2))
```
The function `filter_integers` accepts a list of values and outputs a new list containing only the integers. It uses the `int` as an input to the function and then uses the `type` function to identify the type of each element. The `int()` function is used to convert the value to an integer.