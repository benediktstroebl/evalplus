```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    numbers.sub()  #the rolling_max loop
    numbers.keys()
   
for num, val in zip(numbers, numbers[1:]):
        if val > numbers[0]:
            numbers[0] = val
    return numbers

# Test
test_rolling_max = []
test_numbers = [1, 2, 3, 2, 3, 4, 2]
test_rolling_max.append(max(test_numbers))
print(test_rolling_max)  # Output: [3, 3, 3, 3, 4, 4]
```