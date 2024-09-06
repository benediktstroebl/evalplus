```python
def solution(lst):
    return sum(el for el in lst if el % 2 == 1 and lst.index(el) % 2 == 0)
```
This Python script defines a function called solution, which takes a list of integers as input. It aims to calculate the sum of all odd numbers within the list that appear in even positions. To achieve this, it employs a list comprehension, iterating through each element (el) in the input list (lst). For each element, it checks two conditions: first, whether the element is odd (el % 2 == 1), and second, whether its index in the list is even (lst.index(el) % 2 == 0). If both conditions are true, the element is included in the sum calculated by the sum function, and the result is returned. 

This solution adheres to the problem's specified examples, returning the correct sums for the provided input lists.