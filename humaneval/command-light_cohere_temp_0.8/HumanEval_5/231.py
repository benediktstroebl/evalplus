```python
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + i * delimeter for i, num in enumerate(numbers)]

# Test the function
numbers = [4, 2, 3, 1]
delimiters = [4, 4, 8, 4]  
result = intersperse(numbers, delimiters)

print("Result:", result)

numbers = [1, 2, 3, 4]
delimiters = [4, 8,]  
result = intersperse(numbers, delimiters)

print("Result:", result)
``` 
This script defines a function `intersperse` that takes two arguments: a list of numbers and a single integer `delimiter`. 

The function uses list comprehension to iterate through the numbers list, and for each number, it adds the number multiplied by the current delimiter to the result. The function returns a final list with the interspersed numbers.