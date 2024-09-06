Here is a self-contained Python script that solves the problem of inserting a number 'delimiter' between every two consecutive elements of an input list:
```python
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = []
    for i in range(0, len(numbers)):
        while len(result) > 1 and numbers[i] == numbers[result[-1]]:
            result.append(delimiter)
        result.append(numbers[i])
    result.append(delimiter)
    result.append(numbers[i+1])
    return result
```
The provided Python code defines a function called `intersperse` that takes a list of integers `numbers` and an integer `delimiter` as input and returns a new list with the elements of the input list interspersed with the specified delimiter. This function utilizes a essential while a loop through the input list, and for each element, it checks whether the current element is the same as the last element in the result list. If they are, the current element is appended to the result list with the specified delimiter. Then, the next element of the input list is appended with the specified delimiter and the previous result list.