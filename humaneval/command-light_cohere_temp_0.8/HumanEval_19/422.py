```python
import pytest
from typing import List
def sort_numbers(numbers: List[int]) -> List[str]:
    """
    Sorts the list of numbers from smallest to largest
    :param numbers: list of integers
    :return: list of strings with numbers sorted
    """
    assert isinstance(numbers, List)
    assert len(numbers) > 0
    assert all(isinstance(num, int) for num in numbers)
    assert all(num >= 0 for num in numbers)
    assert sorted(numbers) == [str(num) for num in numbers]
    return [str(num) for num in numbers]
def test_sort_numbers():
    numbers = [3, 1, 5]
    expected = ['one', 'three', 'five']
    got = sort_numbers(numbers)
    assert expected == got
if __name__ == "__main__":
    pytest.py()
```