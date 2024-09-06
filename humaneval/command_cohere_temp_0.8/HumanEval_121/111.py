```python
def solution(lst):
    return sum(x for x in lst if x % 2 == 1 and lst.index(x) % 2 == 0)
```
This Python script provides a function called solution(), which takes a list of integers as input. It aims to calculate the sum of odd numbers present in even positions within the list. To achieve this, it employs a generator expression, created using the sum() function and a conditional clause. This expression filters out odd numbers located in even positions, resulting in the desired sum. The function readily passes the provided tests, demonstrating its correctness.