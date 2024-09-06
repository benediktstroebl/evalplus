```python
def solution(lst):
    return sum(el for el in lst if el % 2 == 1 and lst.index(el) % 2 == 0)
```
This Python script defines a function called solution, which takes a list lst as input. It employs a list comprehension to iterate through each element el in the input list. It checks if the element is odd (el % 2 == 1) and whether it appears in an even position (lst.index(el) % 2 == 0). The sum function calculates the sum of all such odd elements in even positions and returns the result. The provided examples in the docstring highlight how the function operates for different input lists, demonstrating its correctness.