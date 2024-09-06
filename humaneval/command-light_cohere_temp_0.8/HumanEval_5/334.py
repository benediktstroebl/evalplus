Here's a self-contained Python function that solves the problem of inserting a number 'delimiter' between every two consecutive elements of a given list:
```python
def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    result = []
    for i in range(0, len(numbers)):
        if i % 2 == 0:
            result.append(numbers[i]) + delimiter
        else:
            result.append(numbers[i])
    return result
```
The provided Python function called **'intersperse'** takes a list of integers **'numbers'**** and an integer **'delimiter'** as input. It then iterates through list, and between every two consecutive elements, it appends the delimiter to create an spaced list.