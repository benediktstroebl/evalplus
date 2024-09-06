Here's a self-contained Python function that solves the problem of inserting a specified delimiter between every other element in a list:
```python
def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    result = []
    for num in numbers:
        result.append(num)
        delimiter=delimiter
    result.append(num)
    return result
```
This function takes two parameters: a list of integers (numbers) and an integer (delimiter) that represents the value to be inserted between every other element in the list. The function uses a for each element in the input list, appends the element to the result list, and then inserts the delimiter between the two elements. Finally, the function returns the list containing all the elements of the input list, with the specified delimiter between every other element.