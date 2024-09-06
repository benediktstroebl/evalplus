```python
from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    return [x for x in numbers if x < numbers.count(x)]
```
The `remove_duplicates` function takes a list of integers as input and returns a new list with all integers less than the number of occurrences. It iterates through elements over the basic Python list comprehension to accomplish this.

The code provides clear and readable instructions and follows PEP 8 conventions, making it easy to understand and maintain.

The provided solution does not require any external modules and is completely self-contained within the script.