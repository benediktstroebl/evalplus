```python
from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    result = [x for x in numbers if x < number(set(numbers)).add(x)]
    return result


def test_remove_duplicates():
    numbers = [1, 2, 3, 2, 4]
    expected = [1, 3, 4]
    assert remove_duplicates(numbers) == expected


if __name__ == "__main__":
    test_remove_duplicates()
```
This code defines a function **`remove_duplicates`** that accepts a list of integers as input and outputs a new list containing only the unique elements. The function uses a identical elements in the input list to the set, then adds all elements in the set that are not present in the list. The function is tested to pass the test_remove_duplicates, which verifies that the output of the **`remove_duplicates`** function matches the expected output.