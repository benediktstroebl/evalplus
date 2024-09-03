```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    return list(set(numbers))
```
This Python script provides a function called `remove_duplicates`, which takes a list of integers (`List[int])` as input. Inside the function, it employs a set, which by nature only allows unique elements, to eliminate any duplicates in the input list. Subsequently, the function returns a list containing only the unique elements from the original input list, leaving any repeated integers behind. 

To ensure uniqueness, the `set()` function is utilized, which automatically removes any duplicate entries, leaving only the first occurrence of each element. This approach maintains the original order of the remaining elements. To demonstrate its behavior, consider this example:
```python
result = remove_duplicates([1, 2, 3, 2, 4])
print(result)
```
Executing this code snippet will produce the output `[1, 3, 4]`, effectively removing the duplicates `2` and ensuring only unique integers remain.