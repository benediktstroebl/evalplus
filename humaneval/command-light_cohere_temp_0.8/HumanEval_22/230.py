Here is a self-contained Python function that filters integers from a list:
```python
def filter_integers(values):
    return [int(element) for element in values if element.isinstance(int)]
```

This function uses the `isinstance()` function to check if each value in the passed list is an integer. The function then returns a filtered list of integers.

Let's take a sample input list and pass it to the function:
```python
values = ['a', 3.14, 5]
result = filter_integers(values)
print(result)  # Output: [5]
```