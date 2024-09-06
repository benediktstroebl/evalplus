```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any Python values only for integers.
    """
    return [num for num in values if isinstance(num, int)]
```

The function employs a list comprehension that iterates through each element in the input list. It checks if each element is an instance of the int class, and if so, it includes it in the resultant list. Finally, the function returns the filtered list, which only contains elements that are integers. 

Here is an example of how to use the function:
```python
test_list = ['a', 3.14, 5]
print(filter_integers(test_list))  # Output: [5]

test_list2 = [1, 2, 3, 'abc', {}, []]
print(filter_integers(test_list2))  # Output: [1, 2, 3]
``` 

The example usage demonstrates the function's capability to filter out non-integer elements from the given lists successfully.