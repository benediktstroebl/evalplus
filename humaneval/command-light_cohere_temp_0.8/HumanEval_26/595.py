```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ 
    Remove elements that occur more than once from a list of integers.
    """
    function uses Set comprehension to iterate through the list, 
    keeping only the first occurrence of each number.
    return_list = [num for num in numbers if num != numbers.count(num)]
    return return_list
```

In this function, `remove_duplicates` takes a list of integers as an argument. The function uses the `set` comprehension to iterate through the list, and checks if each number is not equal to the count of that number in the `numbers` list. If the number is not found more than once, it adds the number to the `return_list`. 

The function then returns the `return_list`, which contains only the unique occurrences of the numbers in the input list.