```python
def solution(lst):
    return sum(x for x in lst if x % 2 and lst.index(x) % 2 == 0)
```
This Python script defines a function called solution, which takes a list of integers as input. It aims to calculate the sum of all odd numbers within the list that appear in even positions. To accomplish this, it utilizes a generator expression, aided by the index method, to filter out the odd numbers in even positions and then sums them up. The function is self-contained and does not rely on any external variables or assumptions.