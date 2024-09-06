```python
from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    result = [x for x in numbers if x < numbers.count(x)
    unique_numbers]
    return result
numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))  # [1, 3, 4]
```
This code defines a remove_duplicates function that takes a list of integers as input and returns a new list with all distinct integers from the original list. The function utilizes a for- loop to iterate through the input list, and for each element, it checks if the element is equal to any element in the result set, which contains all elements that occur in the input list exactly once. If an element is not equal to any element in the result set, it is added to the result set.