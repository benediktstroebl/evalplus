```python
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = []
    for i, num in enumerate(numbers):
        result.append(num)
        result.append(delimeterme)
        result.append(num)
    return result
```
This Python function called `intersperse` takes a list of integers `numbers` and a delimiter `delimiter` as input and spits the input list into three parts: the original list and two equal `delimiter` spaced parts. 

The function utilizes a for loop to iterate through the input list. It then appends each number in the list to the result list, followed by the delimiter and then another number. 

Finally, the function returns the modified list.