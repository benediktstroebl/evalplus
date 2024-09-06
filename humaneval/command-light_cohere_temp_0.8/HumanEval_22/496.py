Here's a self-contained Python function that filters out integers from a given list of any values:
```python
def filter_integers(values):
    return [x for x in values if isinstance(x, int)]

# Test cases
values1 = ['a', 3.14, 5]
values2 = [1, 2, 3, 'abc', {}, []]

print("Test case 1:", values1)
print(filter_integers(values1))

print("\n")

print("Test case 2:")
values2 = [1, 2, 3, 'abc', {}, []]
print(filter_integers(values2))
```
The function `filter_integers` takes a list of values as input and returns a new list that contains only the integers from the input list. This function uses the IN function to check if a value is of type `int`.  This ensures that only valid integers are included in the output list. 

The output of the code would be:
```
Test case 1: ['a', 3.14, 5]
[5]

```

```
Test case 2: [1, 2, 3, 'abc', {}, []]
[1, 2, 3]
```