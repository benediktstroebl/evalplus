```python
def solution(lst):
    return sum(el for el in lst if el % 2 == 1 and lst.index(el) % 2 == 0)
```
This Python script defines a function called solution, which takes a list of integers as input. It aims to calculate the sum of odd numbers present in even positions within the list. To accomplish this, it employs a list comprehension, iterating through each element (el) in the input list (lst). For each element, it checks two conditions: first, whether the element is odd (el % 2 == 1), and second, whether its index within the list is even (lst.index(el) % 2 == 0). If both conditions are met, the element is included in the sum, and the result is returned. The function's output is the sum of odd numbers in even positions among the list elements.