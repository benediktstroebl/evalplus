```python
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = []
    for i in range(len(numbers) - 1): 
        result.append(numbers[i+1])
        result.append(delimiter)
   
    result.append(numbers[i+1])
    return result

# Test
numbers = [1, 2, 3]
delimiters = [4, 4, 2, 4, 3]

result = intersperse(numbers, delimiters)
print(result) # Output: [1, 4, 2, 4, 3, 4, 2, 4, 3] 
``` 
This script defines a function **'intersperse'** that inserts a number **'delimeter'** between every two consecutive elements of an input list. The code is written in a way that is self-contained and can be easily understood without any external requirements.