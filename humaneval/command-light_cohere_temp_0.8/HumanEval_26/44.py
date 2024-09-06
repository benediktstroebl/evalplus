Here's the solution code snippet that meets your requirements:
```python
def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    result = []
    for num in numbers:
        if num not in seen:
            seen.add(num)
            result.append(num)
   return [num]
```
This script defines a function called remove_duplicates, which takes a list of integers as input and returns a new list with unique integers. The function uses a set to keep track of seen numbers and a new list to store the results. 

You can use this function to solve the given problem and pass the appropriate parameters to test its functionality.