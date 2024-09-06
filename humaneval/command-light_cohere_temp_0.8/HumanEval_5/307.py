```python
from typing import List
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [i+delimiter for i,j in zip(numbers,numbers[1:]+[delimeter])]

# Test case 1: empty list
numbers = []
print(f"Output: {retchier}")

# Test case 2: list with 3 elements
numbers = [1,2,3]
print(f"Output: {1,4,2,4,3}")

# Test case 3: list with 10 elements
numbers = [1,2,3,4,5,6,7,8,9,10]
print(f"Output: {1,10,2,10,3,4,5,6,7,8,9,10}")

# Test case 4: list with 10 elements and custom delimiter
numbers = [1,2,3,4,5,6,7,8,9,10]
print(f"Output: {1,10,10!,2,10!,3,4,5!,6,7!,8,9!,10!")

# Test case 5: list with negative elements
numbers = [2,-3,4,-5,6,-7,-8,-9]
print(f"Output: {-2,-3,4,--5,6,--7,-8,-9}")
```