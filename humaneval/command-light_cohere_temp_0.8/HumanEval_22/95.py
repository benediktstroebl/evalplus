```python
from typing import List

def filter_integers(values):
    """Filter given list of any python values for integers"""
    return [num for num in values if isinstance(num, int)]

# Test cases
values1 = [1, 2, 3, 'abc', }
values2 = [3.14, 5]
result1 = filter_integers(values1)
result2 = filter_integers(values2)

print("Result 1:", result1)
print("Result 2:", result2)
```

The above script defines a function `filter_integers` that takes a list of values and returns a new list containing only the integers from the input list. 

The function uses a list comprehension to filter out the integers from the input list. 

The script then provides two test cases, `values1` and `values2`, passing them to the `filter_integers` function. The function then returns the results `result1` and `result2`, which are the filtered lists of integers from the respective test cases. 

The results are then printed to the console.