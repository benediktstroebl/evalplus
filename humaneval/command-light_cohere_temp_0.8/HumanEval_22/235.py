Here's the self-contained Python function:
```python
def filter_integers(values):
    return [int(x) for x in values if type(x) == int]

# Test cases
test_values = [['a', 3.14, 5], [1, 2, 'abc', {}, []]
test_results = filter_integers(test_values)

print("Test Cases:", test_values)
print("Test Results:", test_results)

```
This script defines a function called **filter_integers** that takes a list of values and returns a new list containing only the integers from the input. It uses a filtered list with type checking for integers.