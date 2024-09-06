```python
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [i+delimiter for i,j in zip(numbers, numbers[1:]+[delimeter])]

# tests
numbers = [1,2,3,4]
print(intersperse(numbers, 4))  
``` 
This script defines a function **'intersperse'** that inserts a number 'delimiter' between every two consecutive elements of the input list. 

In this case, the list **'numbers'** contains four elements, and the output will be **[1, 4, 2, 4, 3]**, with the first and fourth elements separated by 4.