```python
def solution(lst):
    return sum(x for x in lst if x % 2 == 1 and lst.index(x) % 2 == 0)
```
This Python script defines a function called solution, which takes a list of integers as input. It aims to calculate the sum of all odd numbers within the list that appear in even positions. To accomplish this, it employs a generator expression, created with the help of the sum function and a conditional clause. This expression filters out odd numbers located in odd positions, resulting in the desired sum of odd numbers in even positions within the list. The function works effectively and concisely, returning the correct value as specified in the problem description.