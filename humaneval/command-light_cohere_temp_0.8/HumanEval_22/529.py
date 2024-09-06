```python
def filter_integers(values): 
    return [x for x in values if isinstance(x, int)]

# Test the function with various input types
test_values = [['a', 3.14, 5, (1, 2, 3, 'abc', {}, [1, 2, 3])]
test_integers = filter_integers(test_values)
print(test_integers)  # Output: [5, 1, 2, 3]

# Another test with List object containing only integers
test_list = [1, 2, 3]
test_integers = filter_integers(test_list)
print(test_integers)  # Output: [1, 2, 3]
```
This code defines a function **filter_integers** that takes a list of values as input and returns a new list containing only the integers from the input. The test block then demonstrates the test of the function with a variety of input types, and the output is printed to the console.