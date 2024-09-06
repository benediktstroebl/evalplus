```python
from typing import List
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [i+delimiter for i,j in zip(numbers, numbers[1:]) for j in numbers[1:]]
if __name__ == "__main__":
    numbers = [1, 2, 3]
    delimiter = 4
    expected = [1, 4, 2, 4, 3]
    print(f"Expected: {expected}, got: {intersperse(numbers, delimiter)}")
    assert expected == intersperse(numbers, delimiter)
``` 
This code defines a function `intersperse` that separates consecutive elements of a list using a provided delimiter. It then passes thes self-contained function to pass the test for this code, which uses the `numbers` list and the `delimiter` value 4, and prints the expected and actual results.