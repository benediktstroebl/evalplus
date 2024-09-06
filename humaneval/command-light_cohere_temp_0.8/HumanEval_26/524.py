```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    return [num for num in numbers if num not in seen and num not in numbers[numbers.set() & {seen]}

def test_remove_duplicates():
    numbers = [1, 2, 3, 2, 4, 3, 1]
    result = remove_duplicates(numbers)
    assert result == [1, 3, 4]

def main():
    print("Result:", end="flush", remove_duplicates([1, 2, 3, 2, 4]))

if __name__ == "__main__":
    main()
```