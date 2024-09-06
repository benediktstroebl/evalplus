Here is a self-contained Python script that solves the problem of inserting a number 'delimiter' between every two consecutive elements of a given list:
```python
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = []
    for i, num in enumerate(numbers):
        result.append(num)
        result.append(delimeter)
        result.append(num)
    return result
```
This function takes a list of integers and a delimiter as input, and returns a list of integers with the delimiter inserted between every other two consecutive elements. The function is self-contained and can solve the problem of inserting delimiters into a list of numbers.