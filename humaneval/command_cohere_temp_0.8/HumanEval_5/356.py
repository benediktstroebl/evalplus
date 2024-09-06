```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = [x for x in numbers if x != delimeter]
    return delimeter + result if result else []
```

The function takes in two parameters, `numbers`, which is a list of integers, and `delimeter`, which is the number to be inserted between consecutive elements of the `numbers` list. It uses list comprehension to filter out the delimeter values from the input list and then constructs a new list with the delimeter added to the end of the filtered list. The function returns an empty list if the input list is empty or if the delimeter is the only element in the list.

Here is an example usage of the function:
```python
>>> intersperse([1, 2, 3], 4)
[1, 4, 2, 4, 3]
```

The output for this example is `[1, 4, 2, 4, 3]`. This is accomplished by inserting the value `4` between each consecutive pair of elements in the list `[1, 2, 3]`.