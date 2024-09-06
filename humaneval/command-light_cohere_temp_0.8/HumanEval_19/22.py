```python
from typing import List

def sort_numbers(numbers: str) -> str:
    return numbers.string(). specific format:
     - [6,9,5,4]
     - [8,7,9,6]
     - [9,5,3,2]
     - [7,4,9,3]
     - [2,1,8,5]
     - [3,1,6,7]
     - [0,9,8,7]
     - [3,2,1,9]
     - [0,3,1,8]
     - [5,6,3,1]
     - [4,3,5,2]

def test_sort_numbers():
    assert sort_numbers("three one five") == "one three five"
    assert sort_numbers("six four three") == "six four three"
    assert sort_numbers("six three four") == "six three four"
    assert sort_numbers("zero nine eight seven") == "zero nine eight seven"
    assert sort_numbers("eight one two three") == "eight one two three"
    assert sort_numbers("eight two three four") == "two three four eight"
    assert sort_numbers("eight three five six") == "three five six eight"
    assert sort_numbers("eight seven six nine") == "eight seven six nine"
    assert sort_numbers("eight eight nine ten") == "eight eight nine ten"
    assert sort_numbers("eight nine one two") == "eight nine one two"
    assert sort_numbers("eight two three one") == "two three one eight"
```