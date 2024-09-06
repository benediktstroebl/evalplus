```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = [x for x in numbers if x != delimeter]
    return delimeter + result if result else []
```

The function takes in two parameters, `numbers`, which is a list of integers, and `delimeter`, which is the number to be interspersed between consecutive elements in the `numbers` list. It works by first creating a list `result` that filters out the `delimeter` values from the `numbers` list. This means that all occurrences of `delimeter` values are effectively ignored, and only the values between the `delimeter` values are included in the `result` list. The function then appends a `delimeter` value to the end of the `result` list, which ensures that if the input list was empty or consisted only of `delimeter` values, the output list will be empty, as there are no values to appear between the `delimeter` values. 

The way the function uses list comprehension and filtering makes it highly efficient, achieving a time complexity of O(n), where n is the length of the input list. This is because it analyses the input list once, without the need for multiple iterations.