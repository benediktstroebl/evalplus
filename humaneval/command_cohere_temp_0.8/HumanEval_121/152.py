```python
def solution(lst):
    return sum(x for x in lst if x % 2 == 1 and lst.index(x) % 2 == 0)
```
This Python script provides a function called solution(), which takes a list of integers as input. It aims to calculate the sum of odd numbers within even positions in the list. To achieve this, it employs a generator expression, created with the help of the sum() function, which concurrently filters and calculates the sum of relevant elements. The filtering is accomplished by means of the if statement, which focuses on odd numbers (x % 2 == 1) in even positions (determined by lst.index(x) % 2 == 0). As a result, the function returns the desired sum of odd numbers in even positions.