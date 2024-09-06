Here's a Python script with a self-contained function that solves the problem:
```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    return [(x-min(numbers))/(max(numbers)-min(numbers))*1 for x in numbers]
```
The function `rescale_to_unit` takes a list of numbers as input and returns a transformed list where the smallest number is 0 and the largest number is 1.

To make the function robust to a list of numbers with less than two elements, it is recommended to add appropriate exceptions:
```python
def rescale_to_unit(numbers: List[float]) -> List[float]:
    if len(numbers) < 2:
        raise ValueError("List should have at least two elements")
    return [(x-min(numbers))/(max(numbers)-min(numbers))*1 for x in numbers]
```
This way, if a user passes a list of integers `[1,2]` appropriate error message will be raised. 
To better understand the transformation, here is a breakdown of the steps involved in the function:
1.  `min(numbers)`: This finds the smallest number in the list.   
2.  `max(numbers)`: This finds the largest number in the list.  
3.  `x-min(numbers)`: This subtracts the smallest number from each element in the list. 
4.  `max(numbers)-min(numbers)`: This calculates the difference between the largest and smallest number in the list. 
5.  `/(max(numbers)-min(numbers))`: This divides the difference between each number and the smallest by the difference between the largest and smallest number. 
6.  `*1`: This multiplies the result by 1, which essentially does nothing, but is necessary to get the right interpretation of the division. 
7.  `return [(x-min(numbers))/(max(numbers)-min(numbers))*1 for x in numbers]`: This creates a list from the results of the previous calculation and then returns that list. 

This transformation ensures that the smallest number in the list becomes 0 and the largest number becomes 1. You can verify this by running the example test case provided in the problem statement. GIVEN:
List[float] = [1.0, 2.0, 3.0, 4.0, 5.0]
Output:
[0.0, 0.25, 0.5, 0.75, 1.0]

Overall, the function successfully transforms the provided list of numbers such that the smallest number becomes 0 and the largest number becomes 1. 
If the provided list has less than 2 elements, an error is raised to handle this edge case and provide good feedback to the caller.