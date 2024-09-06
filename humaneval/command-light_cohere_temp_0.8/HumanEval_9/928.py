```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    Generates a list of rolling max elements from a given list of integers.
    The rolling max elements are the maximum elements found until the given moment
    in the sequence.
    """

    A rolling max element is the one which is still the max after moving 
    one element forward in the list.
    """
    elements: List[int],
    rolling_max=[]

    max_element = numbers[0]
    rolling_max.append(numbers[i])
    rolling_max.remove(max_element)
    rolling_max.append(numbers[i+1])
    rolling_max.remove(max_element)
    rolling_max.append(numbers[i+2])
    rolling_max.remove(max_element)
    rolling_max.append(numbers[i+3])
    rolling_max.append(numbers[i+4])
    rolling_max.append(numbers[i+5])
    rolling_max = [num for num in rolling_max if num > max_element]

    return rolling_max

``` 
I hope you are welcome to ask any follow-up questions.