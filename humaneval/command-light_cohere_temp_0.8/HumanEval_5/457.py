Here's the self-contained Python script that solves the problem of inserting a number `delimiter` between every two consecutive elements in the input list:
```python
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = []
    for n in numbers:
        if len(result) == 0:
            result.append(n)
        else:
            result.append(delimeter)
    result.append(n)
   return the final list of numbers with the delimiter inserted)
``` 
This function takes a list of integers `numbers` and a delimiter integer `delimeter` as input, and returns a list of integers with the `delimiter` inserted between every two consecutive elements.