```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = []
    for i in range(len(numbers)):
        if i % 2 == 0:
            result.append(numbers[i] + delimeter)
        else:
            result.append(numbers[i])
    return result

# Test cases
numbers = [1, 2,3]
print(inperse(numbers, 4))  # Expected Output: [1,4,2,4,3]

numbers = [1,2,3,4,3]
print(inperse(numbers, 4))  # Expected Output: [1,4,2,4,3,4]

numbers = [1,2,3,4]
print(inperse(numbers, 4))  # Expected Output: [1,4,2,4]

numbers = [1,2,3,4,5]
print(inperse(numbers, 4))  # Expected Output: [1,4,2,4,5]

numbers = [1,2,3,4,6]
print(inperse(numbers, 4))  # Expected Output: [1,4,2,4,6]

numbers = [1,2,3,5]
print(inperse(numbers, 3))  # Expected Output: [1,2,3,5]
``` 
This code defines a Python function called `inperse`, which takes two arguments: a list of numbers and a delimiter integer. The function works by iterating through the input list of numbers, and inserting the delimiter between every two consecutive elements. 

The output of the function is the new list with the elements separated by the specified delimiter. 

The code then provides several test cases to verify the correctness of the `inperse` function.