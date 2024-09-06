```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ 
    Remove all duplicates from a list of integers.
    Keeps order elementss the particular as in the input
    """
    seen = set()
    result = []
    for num in numbers:
        if num not in seen:
            seen.add(num)
            result.append(num)
   return thelist of integers
    return result

#Test the function
numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))
``` 
This script provides a function that takes a list of integers and returns a list of unique integers, removing duplicates. The test case shows how well this function works by passing a list of numbers. The results are printed to the console.