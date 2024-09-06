```python
def solution(lst):
    return sum(x for x in lst if x % 2 == 1 and lst.index(x) % 2 == 0)
```
This Python script defines a function called solution, which takes a list lst as input. It uses a generator expression and the sum function to calculate the sum of odd numbers present in even positions in the list. The index of the list is also used to ensure that the number is in an even position. This is a concise way to solve the problem.