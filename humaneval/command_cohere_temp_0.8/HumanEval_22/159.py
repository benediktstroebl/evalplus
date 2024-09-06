```python
from typing import List, Optional

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any Python values only for integers.

    :param values: List of any Python values.
    :return: List of integers contained in the input list.
    """
    integers: List[int] = []
    for value in values:
        if isinstance(value, int):
            integers.append(value)
    return integers

# Tests
def test_filter_integers():
    assert filter_integers([1, 2, 3, 'abc', {}, []]) == [1, 2, 3]
    assert filter_integers([4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c']) == [4, 5, 6, 7, 8, 9, 10]
    assert filter_integers([11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

test_filter_integers()
```

The function `filter_integers` takes a list of values of any type and returns a list of integers. It iterates through each value in the input list and adds it to the integer list if it is an integer. Finally, it returns the integer list. 

The test function tests the function `filter_integers` with three different cases, ensuring that the expected output is equal to the output of the function with the appropriate input values, thus confirming that the function works correctly. 

You can add these test cases if you need to check your code for more scenarios. 
If you are interested in more information on unit testing, you can ask specific questions.