```python
def solution(lst):
    return sum(el for el in lst if el % 2 == 1 and (len(lst) - lst.index(el)) % 2 == 0)
```
This Python script defines a function `solution` that solves the problem using a lambda expression and the built-in Python `sum` and `index` functions to identify and calculate the sum of odd numbers that appear in even positions in the provided list. 
```python
def solution(lst):
    return sum(el for el in lst if el % 2 == 1 and (len(lst) - lst.index(el)) % 2 == 0)
```