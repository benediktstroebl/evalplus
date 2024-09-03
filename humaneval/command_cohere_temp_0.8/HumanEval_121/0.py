```python
def solution(lst):
    return sum(x for x in lst if x % 2 == 1 and lst.index(x) % 2 == 0)
```
This Python script defines a function called solution, which takes a list lst as input. It aims to calculate the sum of odd numbers present in even positions within the list. To do this, it employs a generator expression, created with the help of the sum function and a conditional statement. This expression filters out odd numbers located in even positions, resulting in the desired sum. The solution function, when executed, returns the sum of odd numbers in even positions within the provided list.