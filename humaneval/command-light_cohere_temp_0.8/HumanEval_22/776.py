```python
def filter_integers(values):
    return [x for x in values if isinstance(x, int)]

#Test cases
values1 = ['a', 3.14, 5]
values2 = [1, 2, 3, 'abc', {}, []]

print(filter_integers(values1))  # Output: [5]
print(filter_integers(values2))  # Output: [1, 2, 3]
```
This code provides a function `filter_integers` that takes a list of values and returns a new list containing only the integers from the input. It uses the specific values to test the correctness of the function. The output will be the value passed into the function and the print statement.