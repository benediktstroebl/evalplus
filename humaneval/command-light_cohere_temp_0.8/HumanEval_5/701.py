```python
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = []
    for i in range(0, len(numbers)):
        if i % 2 == 0:
            result.append(numbers[i] + delimeter)
        else:
            result.append(numbers[i])  
    return result

# Test cases
numbers1 = [1, 2,3]
numbers2 = [4,8,12]
numbers3 = [1,2,3,9]

print(f'Test case 1: {{print(intersperse(numbers1, 4))})
print(f'Test case 2: {print(intersperse(numbers2, 4))})
print(f'Test case 3: {print(intersperse(numbers3, 4))})
```

This function `intersperse` takes a list of numbers and a delimiter as input and returns a list with numbers separated by the delimiter. The function uses an `for` loop to iterate through the list of numbers and adds the current number to the `result` list if the index is even, and simply appends the number to the `result` list if the index is odd. 

The test cases demonstrate the function by passing various lists of numbers with different delimiters and printing the resulting lists.