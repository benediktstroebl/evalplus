Here is a self-contained Python function that solves the problem of inserting a number `delimiter` between every two consecutive elements of an input list:

```python
def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    result = [num for num in numbers if not (len(numbers) == 1 or num != numbers[-1]])
    result.append(delimiter)
    result.append(num)
    for num in numbers[1:]
   return result
```

This function takes a list of integers `numbers` and a number `delimiter` as input and returns a list of integers where a number `delimiter` is inserted between every other pair of consecutive elements.