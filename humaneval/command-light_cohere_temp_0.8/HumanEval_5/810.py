```python
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = []
    for i, num in enumerate(numbers):
        result.append(num)
        result.append(delimeter)
    result.append(num)
    return result
```
This Python function called **'intersperse'** takes a list of integers **'numbers'**** and a integer **'delimeter'** as input. It creates a using a list comprehension to iterate over the input list. It appends each number to the list and then appends the **'delimiter'** to it. The list comprehension also appends the next number to the list, creating the desired effect of inserting a number 'delimiter' between every two consecutive elements.