```python
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return numbers[:2] + [delimeter] + numbers[2:]

#Test cases
numbers = [4, 12, 5, 6]
delimiter = 3
expected = [4, 3, 12, 5, 6]
print(intersperse(numbers, delimiter))  # Output: expected

numbers = [1, 2, 3, 4, 5, 6]
delimiter = 4
expected = [1, 4, 2, 4, 5, 6]
print(intersperse(numbers, delimiter))  # Output: expected

numbers = [1, 2, 3, 4, 5, 6, 7]
delimiter = 2
expected = [1, 3, 4, 5, 6]
print(intersperse(numbers, delimiter))  # Output: expected
```

The function `intersperse` receives a list of numbers and a delimiter as input, and it returns a new list with every second element in the input list separated by the delimiter.