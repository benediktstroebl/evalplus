```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any Python values only for integers.
    """
    result = [x for x in values if isinstance(x, int)]
    return result
```

The above code snippet takes a list of values of any type as input and returns a list of integers. It utilizes list comprehension to iterate over each value in the input list. For each value, it checks if the value is an instance of the integer class using the `isinstance()` function. If it is an integer, the value is included in the resulting list. Finally, the function returns the list of integers it filtered from the input list. 

This function ensures that only integers are retained from the input list, regardless of the original types of the elements.

Here are some example usages of the function to illustrate its behavior:
```python
# Example 1:
input_list = [1, 2, 3, 'abc', {}, []]
result_list = filter_integers(input_list)
print(result_list)  # Output: [1, 2, 3]

# Example 2:
input_list = ['a', 3.14, 5]
result_list = filter_integers(input_list)
print(result_list)  # Output: [5]
```

In the first example, the function filters out the non-integer elements ('abc', {}, []) from the input list, resulting in a list containing only the integers [1, 2, 3]. In the second example, only the integer 5 is retained in the output list, since the other elements are not integers. 

Feel free to use this function to efficiently filter integers from any given list according to your requirements. Let me know if you need further adjustments or have additional questions. I'm here to help!