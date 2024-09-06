```python
def solution(lst):
    return sum(x for x in lst if x % 2 == 1 and lst.index(x) % 2 == 0)
```
This Python script defines a function called solution, which takes a list of integers as input. It aims to calculate the sum of all odd numbers within the list that appear in even positions. To accomplish this, it utilizes a generator expression, aided by the sum function, to iterate through the list and add up values that meet the specified criteria. Notably, the index of the list element is calculated modulo 2 to determine whether it appears in an even or odd position. The function returns the computed sum of odd numbers in even positions as the final result.