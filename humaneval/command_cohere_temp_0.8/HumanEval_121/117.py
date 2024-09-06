```python
def solution(lst):
    return sum(el for el in lst if el % 2 == 1 and lst.index(el) % 2 == 0)
```
This Python script defines a function called solution, which takes a list of integers as input. It aims to calculate the sum of odd numbers within even positions in the list. To achieve this, it employs a list comprehension, iterating through each element in the input list. For each element, it checks two conditions: whether the element is odd (using the modulo operator % to determine divisibility by 2), and whether its index is even (using the modulo operator again, this time with the index). If both conditions are met, the element is included in the sum, resulting in the return of the combined odd values in even positions.