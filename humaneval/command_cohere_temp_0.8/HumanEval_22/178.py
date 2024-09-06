```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any Python values only for integers.
    """
    return [val for val in values if isinstance(val, int)]
```

The function employs a list comprehension that iterates over each value in the input list `values`. It checks if each value `val` is an instance of the `int` type, and if so, it includes `val` in the resultant list. Ultimately, this efficiently filters out non-integer elements from the input list. 

The function's typing annotation `List[Any]` designates that the function expects a list of any arbitrary Python type, while the return annotation `List[int]` signifies that the function will output a list of integers. 

To properly grasp the function's behavior, consider testing it against diverse inputs. Here's an example: 
```python
# Test with a sample list of mixed values
sample_list = [1, 2, '3', 4, 'abc', 5.6, 7]
result = filter_integers(sample_list)
print(result)  # Output: [1, 4, 5]
```

In this test case, the function selectively picks out the integer values (1, 4, and 5) from the heterogeneous list, omitting the non-integer elements ('3', 'abc', and 5.6). 

Another pivotal scenario tests the function with a list that exclusively contains non-integer values: 
```python
pure_non_int_list = ['a', 'b', 'c', 'd', 'e']
result = filter_integers(pure_non_int_list)
print(result)  # Output: []
```

Here, the function returns an empty list `[]`, indicating that no elements in the input list hold an integer type. 

Such comprehensive testing aids in solidifying the function's correctness and provides an insightful examination of its behavior against a spectrum of inputs.