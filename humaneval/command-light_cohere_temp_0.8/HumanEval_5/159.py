Here's a self-contained Python function that solves your problem:
```python
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimiter' between every two consecutive elements of input list.
    :param numbers: list of integers
    :param delimiter: int
    -> list of integers
    """
    return [num + delimiter for num, delimiter in zip(numbers, [delimeter] * (len(numbers) // 2))]

# Test the function with different inputs
numbers = [4, 2, 8, 3, 1]
result = intersperse(numbers, 2)
print(result)  # Expected output: [4, 2, 8, 6, 4, 3, 7]
```
This Python function, `intersperse`, takes a list of integers and a delimiter as input. It iterates through code in a way that every two consecutive elements are separated by the provided delimiter. The test case demonstrates how the example usage.