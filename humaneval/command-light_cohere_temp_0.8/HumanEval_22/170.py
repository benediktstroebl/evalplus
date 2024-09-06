Here's a self-contained Python script that filters integers from a given list:
```python
def filter_integers(values):
    # Filter out non-integer values
    values = [v for v in values if isinstance(v, int)]
    
    # Check if any element is missing
    if not values:
        return []
    
    # Return list of integers
    return values

# Example usage
values1 = ['a', 3.14, 5]
filtered1 = filter_integers(values1)
print(filtered1)  # Output: [5]

values2 = [1, 2, 3, 'abc', {}, []]
filtered2 = filter_integers(values2)
print(filtered2)  # Output: [1, 2, 3]
```
This script defines a function `filter_integers` that takes a list of values as input and returns a new list that contains only the integers from the input.