Here is a self-contained Python script that solves the problem of filtering integers from a given list:
```python
def filter_integers(values):
    return [x for x in values if isinstance(x, int)]

# Test the function
test_values = [1, 2, 3, 'abc', {}, [5], [3.14] ]
 test_filter = filter_integers(test_values)
assert len(test_filter) == 10
```
The code defines a function **filter_integers** that takes a list of values and returns a new list containing only the integers from the input. This is using the filtering, the function applies the isinstance() condition to check if each element in the input list is an integer. The test_filter variable is created with a sample list of values, and the function is called with this list. The assert statement is used to check the length of the returned list, ensuring that it contains 10 elements, which corresponds to the list having only integers.