```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + i * delimeter for i, num in enumerate(numbers)]

# Test cases are self-contained within the script
test_intersperse = {
    "test_case_1": [],  # Empty list
    "test_case_2": [1, 2, 3],  # List with numbers
    "test_case_3": [1, 2, 3, 4, 5],  # Longer list with duplicates
    "test_case_4": [1, 2, 3, 3, 4, 5],  # Same list but different order
    "test_case_5": [1, 2, 3, 9],  # Duplicate numbers
    }

# Function call and results are printed to console
for test_name, test_values in test_cases.py

print(f"{test_name} =>")
for val, n in zip(test_values, [i * delimeter for i in range(len(test_values))]):
    print(f"{val} -> {n}")
```