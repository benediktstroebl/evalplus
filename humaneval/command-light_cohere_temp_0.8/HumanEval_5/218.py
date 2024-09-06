```python
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [i+delimeter for i,j in zip(numbers,numbers[1:])]

#Test case 1
numbers = [1, 2, 3]
print(intersperse(numbers, 4))
#Expected Output: [1, 4, 2, 4, 3]

#Test case 2
numbers = [4,5,6]
print(intersperse(numbers, 4))
#Expected Output: [4, 8, 5, 6]

#Test case 3
numbers = [1,2,3,4]
print(intersperse(numbers,2))
#Expected Output: [1, 3, 5, 7]

#Test case 4
numbers = [4, 5, 6, 7]
print(intersperse(numbers, 3))
#Expected Output: [4, 7, 5, 9, 6]
```
This script defines a function `intersperse` that inserts a number `delimiter` between every two consecutive elements of the input list.  `numbers` are method works by creating a `zip` between elements and inserting the `delimiter` at the end of the second element, resulting in an ordered list with the required format.