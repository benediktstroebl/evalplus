```python
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + i * delimeter for i, num in enumerate(numbers)]

# Test the function with some examples
numbers = [1, 2, 3]
delimiter = 4
result = intersperse(numbers, delimiter)
print("Result:", result)

numbers = [4, 5, 6]
delimiter = 3
result = intersperse(numbers, delimiter)
print("Result:", result)

numbers = [10, 20, 30]
delimiter = 7
result = intersperse(numbers, delimiter)
print("Result:", result)
```
This script defines a function `intersperse` that takes a list of numbers and an integer `delimiter` as parameters. The function uses a `enumerumerate()` and a list comprehension to achieve the desired result: inserting a number `delimiter` between every two consecutive elements of the input list.