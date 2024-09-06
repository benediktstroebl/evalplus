Here is a self-contained Python script that defines a function filter_integers that filters out non-integer values from a given list: 
```python
import typing

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any python values only for integers.

    Args: 
        values: a list of any python value, can be integers or not

    Returns: 
        list: list of integers only
    """
    return [x for x in values if isinstance(x, int)]

# Testing the function
test_values = [1, 2, 3, 'abc', 123, []]
result = filter_integers(test_values)
print(result)  # Output: [1, 2, 3]
```
The function takes a list of values as an argument and returns a new list containing only the integers present in the input list. This is filtering is done using a generator expression and the isinstance() function.