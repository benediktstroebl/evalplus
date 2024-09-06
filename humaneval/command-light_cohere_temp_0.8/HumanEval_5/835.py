```python
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = []
    for i in range(0, len(numbers)):
        if i % 2 == 0:
            result.append(numbers[i] + delimeter)
        else:
            result.append(numbers[i])
    return result

# Test case using sample input
test_numbers = [1, 2,3,4,5]
test_delimiter = 4
test_result = intersperse(test_numbers, test_delimiter)
print(test_result)
```  This Python function, `intersperse`, takes a list of integers and a delimiter as input and returns a new list with the integers interspelled by the specified delimiter. The function uses a loop to iterate through the input list, checking if the current index is even or odd. If the index is even, the function appends the current element to the result list along with the delimiter. If the index is odd, the function appends the current element as it is without the delimiter. The function then returns the list with the interspelled elements.