```python
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + i * delimeter for i, num in enumerate(numbers)]

# Test the function with a list of numbers and a delimiter
numbers = [1, 2, 3]
delimiter = 4
result = intersperse(numbers, delimiter)

# Print the results
print(f"Input: {scient(join(format)}) Output: {result}")
``` 
This Python function, **'intersperse'**, is designed to take a list of numbers and a delimiter as input and return a new list with the numbers separated by the provided delimiter. The function uses the specific function that adds the delimiter value to each element in the list, effectively separating every two consecutive elements with the specified delimiter.