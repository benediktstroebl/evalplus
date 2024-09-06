```python
def solution(lst):
    return sum(el for el in lst if el % 2 == 1 and lst.index(el) % 2 == 0)
```
This Python script defines a function called solution, which takes a list lst as input. It aims to calculate the sum of odd numbers present in even positions within the list. To accomplish this, it employs a list comprehension, iterating through each element el in the input list. It checks two conditions for each element: whether the element is odd (el % 2 == 1) and whether its position in the list is even (lst.index(el) % 2 == 0). When both conditions are met, the element is included in the sum, and the result is returned as the output. This code efficiently solves the problem as specified in the prompt.