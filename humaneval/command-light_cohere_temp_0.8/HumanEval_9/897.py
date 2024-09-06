```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    max_so_far = numbers[0]
    max_ending = numbers[0]
    result = [max_so_far]
    for num in numbers[1:]:
        if num > max_ending:
            max_ending = num
        elif num == max_ending:
            max_ending += 1
        result.append(max_ending)
    return result
# Test cases
numbers1 = [1, 2, 3, 4, 5]
numbers2 = [3, 4, 5, 6, 7]
result1 = rolling_max(numbers1)
result2 = rolling_max(numbers2)

print(f"Test 1: Maxending number across all moments in numbers1: {result1}")
print(f"Test 2: Maxending number across all moments in numbers2: {result2}")
 ``` 
This code defines a function called rolling_max, which takes a list of integers as input and returns a new list that contains the maximum value encountered up to each moment in the original list. The code also provides test cases to verify the functionality of the rolling_max function, and the results are printed out.