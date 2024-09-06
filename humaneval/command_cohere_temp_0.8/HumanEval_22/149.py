```python
from typing import List

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any Python values only for integers.
    """
    result = [x for x in values if isinstance(x, int)]
    return result
```

The above code snippet takes a list of various values as input and returns a list that contains only the integer values from the original list. It utilizes Python's list comprehension capability in conjunction with the `isinstance()` function to generate the resultant list. 

If you would like to test this code, you can create a script that incorporates the `filter_integers` function and include respective test cases as below:
```python
filter_integers(['a', 3.14, 5])
>> [5]

filter_integers([1, 2, 3, 'abc', {}, []])
>> [1, 2, 3]
``` 

This would help verify that the function performs the filtration appropriately. 
If you prefer to use pytest for testing, you can do it as well:
```python
def test_filter_integers():
    assert filter_integers(['a', 3.14, 5]) == [5]
    assert filter_integers([1, 2, 3, 'abc', {}, []]) == [1, 2, 3]
``` 
This approach provides better coverage of test cases, and the assert statements make the code more readable and understandable.