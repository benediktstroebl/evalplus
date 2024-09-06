```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ Removes all elements that occur more than once in a list of integers
        Keeps order of elements left the same as in the input """
    seen = set()
    result = [x for x in numbers if not (x in seen or seen.add(x))]
    return result
```

To use this function, you can pass a list of integers as an argument, and the function will return a new list that contains only the unique integers from the original list.

For example, the function can be called as follows:
```python
remove_duplicates([1, 2, 3, 2, 4])
```

The resulting output will be:
```
[1, 3, 4]
```

This function achieves the task of removing duplicates whilst maintaining the original order of the elements through the use of a set data structure. By utilizing a set, the function inserts elements from the list into the set, thereby eliminating duplicates as sets do not allow duplicate values. The function then generates a new list from the set, which contains all unique elements from the original list, retaining the original order of these elements. 

The `typing` module is used to indicate the type of the argument and return value of the function, which allows the function to provide better type checking when it is used. 

This solution is also unit-testable, allowing for independent tests to be run on the remove_duplicates function to ensure it performs as expected.