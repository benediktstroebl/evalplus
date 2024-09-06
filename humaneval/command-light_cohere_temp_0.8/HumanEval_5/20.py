```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = []
    for i in range(len(numbers)):
        if i % 2 == 0:
            result.append(numbers[i]+delimiter)
        else:
            result.append(numbers[i])
    return result

#Test case
test_numbers = [1, 2,3,4,5]
test_delimiter = 4
test_result = intersperse(test_numbers, test_delimiter)
print(test_result)

test_numbers = [4,4,4,4]
test_delimiter = 4
test_result = intersperse(test_numbers, test_delimiter)
print(test_result)
```
The function `intersperse` takes a list of integers and a delimiter as input and returns a new list where the consecutive even indices of the input list are separated by the delimiter. The output is the provided test cases.