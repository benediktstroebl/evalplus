Here is a self-contained Python script that solves the problem of filtering integers from a given list:

```python
def filter_integers(values: List[Any]):
    return [x for x in values if isinstance(x, int)]

# Test cases
test_values = [['a', 3.14, 5, 1, 2, 3, 'abc', {}, []]
test_results = filter_integers(test_values)

print("Test Results:", test_results)
```

The `filter_integers` function filters a list of any Python values and returns a new list containing only the integers. It uses the value filtering technique, which checks each element's `isinstance` int to determine if it's an integer or not. The function then returns a filtered list of integers.