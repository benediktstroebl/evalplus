```python
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = []
    for i in range(len(numbers)):
        if i % 2 == 0:
            result.append(numbers[i]+delimeter)
        else:
            result.append(numbers[i])
    return result
``` 
This function takes a list of integers and a delimiter as input and returns a new list with the numbers interspersed with the delimiter. The function uses a list comprehension and the modulo operator to achieve this effect.