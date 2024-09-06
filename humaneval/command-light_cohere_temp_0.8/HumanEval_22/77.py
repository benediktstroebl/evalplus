```python
def filter_integers(values):
    return [num for num in values if isinstance(num, int)]

# Test cases
test_values = [['a', 3.14, 5], [1, 2, 'abc', [], {}]
test_results = filter_integers(test_values)

print("Test case 1:", test_results)
print()

test_values2 = [1, 2, 3, 'abc', {}, []]
test_results2 = filter_integers(test_values2)

print("Test case 2:", test_results2)
``` 
This script defines a function called `filter_integers` that takes a list of values and returns a new list containing only the integers from the input. The function uses the filter implementation with `isinstance` to only include elements that are integers in the output.

The test cases are defined with lists of values, and the `filter_integers` function is called on these lists. The test results are then printed to the console, demonstrating the correct filtering behavior.