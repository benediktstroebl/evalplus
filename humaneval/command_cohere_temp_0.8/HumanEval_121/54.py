```python
def solution(lst):
    return sum(x for x in lst if x % 2 == 1 and lst.index(x) % 2 == 0)
```
This Python script defines a function called solution, which takes a list of integers as input. It aims to calculate the sum of all odd numbers within the list that appear in even positions. To achieve this, it employs a generator expression, filtered by the condition x % 2 == 1 and lst.index(x) % 2 == 0. The index() method is used to determine the position of each number within the list. Thus, the sum is correctly computed and returned.