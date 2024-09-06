Here's a self-contained Python function that implements the `intersperse` function from the prompt:
```python
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    numbers = list(numbers)  # Convert input list to list of integers
    result = [num] + [delimeter] + [num + delimeter] * (len(numbers) - 2) + [delimeter] + [num] 
    return result[:]  # Return only the constructed list

# Test cases
numbers1 = [4, 12, 5, 6]
numbers2 = [1, 2, 3]
print(intersperse(numbers1, 4))  # Expected output: [4, 8, 12, 16, 20]
print(intersperse(numbers2, 4))  # Expected output: [1, 2, 3, 8, 11]
```
This function will insert the specified `delimiter` between every two consecutive elements in the input list. 
The output will be the list that is the correct result of the operation, as expected by the function.