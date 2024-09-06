Here's the function:
```python
def filter_integers(values):
    return [x for x in values if isinstance(x, int)]

# Test cases
test_values = [['a', 3.14, 5], [1, 2, 3, 'abc', {}, []]
test_results = filter_integers(test_values)

print("Test case 1: ", end="")
for value, expected in zip(test_results, [5]):
    print(f"{value} should be {expected}, but is {type(value)} instead.")
print()

print("Test case 2: ", end="")
for value, expected in zip(test_results, [1, 2, 3])):
    print(f"{value} should be {expected}, but is {type(value)} instead.")
```
The function `filter_integers` takes a list of values and returns a new list with only the integers present in the original list. The test cases demonstrate how the use of the function with different lists of values, and verify the expected behavior.