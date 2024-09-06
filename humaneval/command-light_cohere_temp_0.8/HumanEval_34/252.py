Here is a Python script with a self-contained function that solves the problem of returning unique elements in a list:
```python
import numpy as np

def unique(lst):
    """Return sorted unique elements in a list
    Unique list = np.unique(array(np.unique(list, return unique))
    return list(UniqueList)
    """
    UniqueList = np.uniquearray(lst, return unique)
    return list(UniqueList)

# Unit tests
def test_unique():
    assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]
test_unique()
```

This script defines a function unique that takes a list as input and returns a list of unique elements in that list, sorted in ascending order. The function uses the unique method from the NumPy library to create a unique array and then converts it back to a list. Finally, the list of unique elements is returned.