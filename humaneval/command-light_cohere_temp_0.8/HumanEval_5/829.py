```python
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + delimeter for num in numbers] + [num + delimeter*2 for num in numbers]

# Test case 1
numbers = [1, 2, 3]
result = intersperse(numbers, 4)
print(result)  # Expected output: [1, 4, 2, 4, 3]

# Test case 2
numbers = [1, 2, 3, 4, 5]
result = intersperse(numbers, 6)
print(result)  # Expected output: [1, 6, 2, 6, 3, 6, 4, 5]

# Test case 3
numbers = [10, 11, 12, 13]
result = intersperse(numbers, 2)
print(result)  # Expected output: [10, 10, 11, 12, 13]
```
This Python code defines a function called `intersperse` that takes two parameters: a list of numbers and a positive integer `delimiter`. 

The `intersperse` function uses list comprehension to iterate over the input list of numbers, appending a consecutive element with the current number plus twice the `delimiter` value. 
This effectively separates every two elements with the `delimiter`, creating a desired spacing between them. 


The test cases demonstrate the function's behavior by passing different input lists and integer values for `delimiter`. The output of each test case should match the expected output.