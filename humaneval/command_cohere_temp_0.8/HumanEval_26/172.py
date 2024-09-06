```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    return list(dict.fromkeys(numbers))
```
This Python script provides a function called `remove_duplicates`, which takes a list of integers as input and returns a new list that excludes any duplicate integers. Before giving a detailed explanation, let's go through the main components of the code:
1. `from typing import List`: This line imports the `List` module from the `typing` module. It allows you to define what kinds of parameters a function accepts, signaling to users that the function expects a list of integers.
2. `def remove_duplicates(numbers: List[int]) -> List[int]`: This defines a function called `remove_duplicates` which takes a list of integers (`List[int])`, and returns a new list of integers.
3. `return list(dict.fromkeys(numbers))`: This is the core of the unique elements removal. Here's how it works:
    - `dict.fromkeys()` turns the list into a dictionary, where each unique element from the list is a key, and its count is the corresponding value.
    - `list()` converts the dictionary back into a list.
    - Any elements that occurred more than once in the original list will not be included in the new list because they will not be present in the new dictionary.

Therefore, this single line of code efficiently removes duplicate elements and retains the order of unique elements as stipulated by the problem statement.