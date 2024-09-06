```python
from typing import List

def filter_integers(values:
    """ 
        filtered_int = [x for x in values if isinstance(x, int)]
        return filtered_int
    """

def test_filter_integers():
    assert filter_integers(['a', 3, 'four', 5]) == [5]
    assert filter_integers([1, 2, 3]) == [1, 2, 3]
    assert filter_integers([1, 2, 'three', 5]) == [1, 2]
    assert filter_integers([1, 2, 3, 'a']) == []
 ```
The provided code defines a function `filter_integers` that filters out any values in the given list that are not of type `int`. The function uses a list comprehension to iterate through each element in the input list. It creates ais filter_integers function and adds a docstring that explains what the function does.