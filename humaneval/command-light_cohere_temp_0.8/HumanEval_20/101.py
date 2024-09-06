```python
from typing import List

def find_closest_elements(numbers: List[float]):
    numbers.sort()
    smallest = numbers[0]
    largest = numbers[0]
    for num in numbers[1:]:
        if num < smallest or num > largest:
            smallest = num
            largest = num
    return largest, smallest

def test():
    numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 6.2]
   2)
    smaller, larger = (find_closest_elements(numbers), return_values=True))
    assert smaller is None
    assert larger is not None
    assert [1.0] < larger
    smaller, assert 1.0 < larger
   

    def main():
        numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 6]
        print(smaller, larger)
```