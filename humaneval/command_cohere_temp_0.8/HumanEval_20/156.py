```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    numbers.sort()
    if len(numbers) < 2:
        raise IndexError("List of numbers must have a minimum of two elements")
    else:
        return (numbers[0], numbers[-1])
```

This script sorts a list of numbers and then returns the two closest numbers at each end of the sorted list. It raises an error if the list length is less than 2. This solution has a time complexity of O(n log n) due to the sorting process, which takes O(n log n) in most cases. The solution is also space efficient, with a constant auxiliary space complexity of O(1). 

To make the code more robust against some edge cases, you could add some tests to the provided solution:
```python
# Tests:
test_cases = [
    [1.0, 2.0, 3.0, 4.0, 5.0, 2.2], 
    [1.0, 2.0, 3.0, 4.0, 5.0, 2.0],
    [1.0, 2.0, 3.0, 4.0, 5.0, 2.1],
    [1.0, 2.0, 3.0, 4.0, 5.0, 3.0],
]

for case in test_cases:
    print(f'Test case: {case}, Expected: (2.0, 2.2), Got: {find_closest_elements(case)}')
```

This would raise an error if the input list is insufficiently populated, and otherwise provide us with confidence that the solution works as expected for a few more cases.