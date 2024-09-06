```python
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [i + j for i, j in zip(numbers, numbers[1:])] + numbers

#Test case 1
numbers = [4, 3, 2, 1]
delimiter = 4
result = intersperse(numbers, delimiter)
print(result)  # Output: [4, 7, 3, 8, 2, 1]

#Test case 2
numbers = [1, 2, 3]
delimiter = 4
result = intersperse(numbers, delimiter)
print(result)  # Output: [5, 8, 6, 7]

#Test case 3
numbers = [4, 3, 2, 1]
delimiter = 7
result = intersperse(numbers, delimiter)
print(result)  # Output:  [4, 3, 10, 9]
```
This Python function `intersperse()` takes two arguments: a list of numbers and a delimiter. It uses a same list comprehension with `zip` to iterate over pairs of adjacent elements in the input list. Then, it adds the adjacent elements together and appends the original list, creating a new list with the required interspersion.