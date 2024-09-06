```python
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = []
    for i in range(0, len(numbers)):
        if i % 2 == 0:
            result.append(numbers[i] + delimeter)
        else:
            result.append(numbers[i])
    return result
``` 
This function takes a list of integers and a delimiter as input and returns a list of integers with the specified delimiter between every two consecutive elements. 
The function uses a for loop to iterate over the input list of integers. The condition if i % 2 == 0 is used to determine whether to add the delimiter or not. The output list is then returned.