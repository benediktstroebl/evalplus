```python
def solution(lst):
    return sum(x for x in lst if x % 2 == 1 and lst.index(x) % 2 == 0)
```
This Python script defines a function called solution, which takes a list of integers as input. It aims to calculate the sum of odd numbers within even positions in the list. To achieve this, it employs a generator expression, created using the sum function and a generator expression. This expression filters elements that are odd and positioned at even list indices. The index of an element in a list is determined using the index function. The resulting sum represents the total of odd numbers in even positions in the provided list.