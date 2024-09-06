```python
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = []
    for i in range(0, len(numbers)):
        if i % 2 == 0:
            result.append(numbers[i])
        else:
            result.append(numbers[i] + delimeter)
    return result

# Test cases for the function
numbers = []
numbers.append([1, 2, 3, 4, 5])
numbers = [6, 7, 8, 9, 10]

result = intersperse(numbers, 2)
print(result)  # Expected output: [2, 4, 6, 8, 10, 7]
``` 
The function '**`intersperse`**' takes a list of numbers and a delimiter as input, and returns a new list with the numbers separated by the delimiter. This function uses a simple logic to determine whether to append the next number or append the current number followed by the delimiter.