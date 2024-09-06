```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    result = [x for x in numbers if x not in seen and not seen.
    seen.add(x)()
   
    return result

# Test cases
test_data = [1, 2, 3, 2, 4,3,4,5]
test_result = remove_duplicates(test_data)
print("Test Result:", test_result)

test_data2 = [1, 1, 2, 2, 2, 2, 3, 4]
test_result2 = remove_duplicates(test_data2)
print("Test Result 2:", test_result2)
```
The solution provided above is a simple yet efficient way to remove duplicates from a list of integers using a set. The provided test cases demonstrate how the can be used to test the correctness of the function.