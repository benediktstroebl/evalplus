```python
from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    return [num for num in numbers if num not in numbers[numbers.set()]]
Here is a self-contained Python script that solves the problem you provided in the prompt. The remove_duplicates function takes a list of integers as input and returns a new list with the unique integers from the input list. This is also removes any duplicates from the list.