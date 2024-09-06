```python
from typing import List
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimiter' between every two consecutive elements of input list. """
    
    - Step 1: Initialize an empty list to store the output
    output_list = []
    
    - Step 2: Iterate over the input list
    for num in numbers:
        - Step 3: If it's the first element, add the delimiter to the output list
        - Step 4: Append the current element to the output list
        - Step 5: If the current element is the last element in a sequence of two, add the delimiter to the output list
        
        output_list.append(num)
    num)
       output_list.append(delimiter)
       output_list.append(num)
        
    return output_list
    
# Unit tests:
input_list = [1, 2, 3]
result = intersperse(input_list, 4)
test_list = [1, 4, 2, 4, 3]
assertEqual(result, test_list)
input_list = [1, 2, 3, 4]
result = intersperse(input_list, 4)
test_list = [1, 4, 2, 4, 3, 4]
assertEqual(result, test_list)
input_list = [5, 6, 7]
result = intersperse(input_list, 4)
test_list = [5, 10, 6, 10, 7]
assertEqual(result, test_list)
```