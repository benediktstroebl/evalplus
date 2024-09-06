```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    From a given list of integers, generates a list of rolling 
    maximum elements found until a given moment in the sequence.
    : Returns a maximum list of integers in the order of increasing
    potential maximum, and the list will not be sorted.
    """
    list of integers is a list of numbers, and numbers could be 
    negative. The rolling max function will return a list of numbers, 
    starting from the beginning of the list, and will keep returning 
    the element with the maximum value until the current element becomes 
    the maximum.
    """ 

 numbers: List[int]
    """
    return [num for num, i in zip(numbers, numbers[1:]) ][i]
``` 
We start by creating a generator expression with a zip function to iterate over the numbers list and the numbers_up_list list simultaneously. Then, we use the names to map each number from numbers_up_list to the index i of numbers. We get the maximum value at each number from numbers, and the list is returned.