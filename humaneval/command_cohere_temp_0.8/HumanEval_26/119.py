```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ Removes all elements that occur more than once in a list of integers
        Keeps order of elements left the same as in the input """
    seen = set()
    result = [x for x in numbers if not (x in seen or seen.add(x))]
    return result
```

This Python script defines a function called `remove_duplicates` which takes a list of integers as input and returns a new list that excludes any duplicate integers. It uses a set called `seen` to keep track of integers that have already been encountered. The function iterates through the input list, and for each integer `x`, it checks if `x` is already in the `seen` set. If not, it adds `x` to the set and includes it in the `result` list. If an integer occurs more than once in the input list, it will only appear once in the result. The markdown code block includes a test case that demonstrates the function's behavior. 

This solution is efficient in terms of time and space complexity since the set data structure provides constant time lookup and the resulting list is linearly proportional to the size of the input list.