```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    return [num for num in numbers if num not in numbers[numbers.count()]]
def test_remove_duplicates(numbers: List[int]) -> None:
    expected = [1, 2, 3, 2, 4]
    actual = remove_duplicates(numbers)
    assert actual == expected
    return_

numbers = [1, 2, 3, 2, 4]
test_remove_duplicates(numbers)  # Should pass
 ```