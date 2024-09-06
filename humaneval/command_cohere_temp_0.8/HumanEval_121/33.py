```python
def solution(lst):
    return sum(x for x in lst if x % 2 == 1 and lst.index(x) % 2 == 0)
```
This Python script provides a function called solution(), which takes a list of integers as input. It aims to calculate the sum of odd numbers within even positions of the list. To accomplish this, it utilizes a generator expression, created with the help of the sum() function, along with a conditional statement. This expression filters out odd numbers situated in even positions, contributing to the final sum. The result is the total value of odd numbers in even positions within the provided list.