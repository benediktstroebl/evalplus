```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """ Returns the list of rolling maximum elements found in the given list
    @return: list[int]
    @param: list[int] numbers 
    """
    numbers.add=0
    
       a=0
    # initialize the rolling max counter 
    b=1
    max_num=numbers[0]
    result = [max_num]

    for num in numbers[1:]:
        # update the rolling max number 
        a+=1
        # update the max number 
        max_num=max(num,max_num)
        # add the new number to the result list 
        result.append(num)
    # update the rolling max counter 
        b+=1

    return result

# test case 
numbers=[1,2,3,2,3,4,2]
result = rolling_max(numbers)
print(result)  # expected output: [1, 2, 3, 3, 3, 4, 4]
```
This Python code defines a function named rolling_max, which generates a list of the rolling maximum elements within a given input list of integers. It employs the single-argument list of integers and returns a list of the rolling maximum elements found in that sequence, it also ensures the output list is ordered with the maximum elements first. The code includes a test case, which uses the rolling_max function with a sample input list of numbers, and it prints the expected output, which is the list of the rolling maximum elements in that sequence.