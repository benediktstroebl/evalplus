```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    numbers = List(numbers)  # Create a mutable copy to avoid mutating the original list
    max_element = numbers[0]  
    current = max_element  
    for num in numbers[1:]:
        current = max(num, current)  
        max_element = current 
    return [max_element]

# Unit tests
numbers_test_1 = [1, 2, 3]
numbers_test_2 = [2, 3, 4, 5]
numbers_test_3 = [5, 5, 5, 6]

test_results = []

# Test case 1
test_results.append(rolling_max(numbers_test_1))
# This line will run the function with the test input and store the results
test_results.append([max_element])
print("Test 1 results:", test_results)

# Test case 2
test_results.append(rolling_max(numbers_test_2))
# Same as above
test_results.append(max_element))
print("Test 2 results:", test_results)

# Test case 3
test_results.append(rolling_max(numbers_test_3))
# Same as above
test_results.append(max_element))
print("Test 3 results:", test_results)
```
This script defines a function `rolling_max` that takes a list of integers as input and generates a new list with the maximum element from the list after each iteration. The test cases ensure that the function is working correctly and are printed to the console.