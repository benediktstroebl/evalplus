```python
def filter_integers(values):
    return [x for x in values if isinstance(x, int)]

# Test the function
values = ['a', 3.14, 5, 1, 2, 3, 'abc', {}, []]
print("Filtered values:", values)
print("Should be integers:", filter_integers(values))
``` 
This code defines a function called `filter_integers` that filters a list of values to only include integers. 

It then tests the function by passing the values list, and the expected output is printed.