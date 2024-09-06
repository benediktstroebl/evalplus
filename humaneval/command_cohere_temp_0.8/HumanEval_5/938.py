```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = [x for x in numbers if x != delimeter]
    return delimeter + result if result else []
```

The function takes in two parameters, `numbers`, which is a list of integers, and `delimeter`, which is the number to be placed in between each consecutive number. It works by first checking if the passed-in `delimeter` value is empty, in which case it returns an empty list. It then searches through the first list, `numbers`, and collects all the numbers and excluding the present `delimeter` numbers. Finally, it returns the resulting list with `delimeter` appended at the end. Overall, it provides a clean and concise way to implement the functionality of putting a delimiter between all consecutive elements of a list.