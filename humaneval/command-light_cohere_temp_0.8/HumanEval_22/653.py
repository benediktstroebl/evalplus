```python
def filter_integers(values): 
    return [num for num in values if isinstance(num, int)]

# Test cases
values1 = ['a', 3.14, 5]
values2 = [1, 2, 3, 'abc', {}, []]

print(filter_integers(values1))  # Expected Output: [5]
print(filter_integers(values2))  # Expected Output: [1, 2, 3]
```

The function filter_integers takes a list of values as input and returns a new list that contains only the integers from the input list. It uses the value of the list comprehension and the isinstance() function to filter out non-integer values. This function can be used to pass all the standard tests and is self-contained, meaning it doesn't rely on any other functions or modules.