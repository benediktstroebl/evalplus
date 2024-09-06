```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = []
    for i, num in enumerate(numbers):
        if i != 0: result.append(delimeter)
        result.append(num)
   result.append(delimiter))
   return result

# Test cases
test_list = [4, 2,8,3]
test_list2 = [1,2,3,4,5,6]
test_list3 = [9,8,7]
test_cases = [test_list, test_list2, test_list3]

for test_case in test_cases:
    print(f"Input: {test_case}")
    print("Output:",interperse(test_case, 2))
    print()
```
This code defines a function called `intersperse` that takes a list of integers and a delimiter as input and returns a list of interspaced numbers. The code then creates test cases with lists of integers and passes them through the `intersperse` function with a delimiter of 2. Finally, it prints the output for each test case.