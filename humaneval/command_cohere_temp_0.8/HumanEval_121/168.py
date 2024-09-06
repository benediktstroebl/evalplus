```python
def solution(lst):
    return sum(x for x in lst if x % 2 == 1 and (len(lst) - lst.index(x) - 1) % 2 == 0)
```
This Python script defines a function called solution, which takes a list of integers as input. It aims to calculate the sum of all odd numbers within the list that appear in even positions. To achieve this, it employs a generator expression, filtered by the condition "x % 2 == 1," which selects all odd numbers in the list. The second condition, "(len(lst) - lst.index(x) - 1) % 2 == 0," checks whether the odd number appears in an even position by evaluating the parity of the position index. The sum function then aggregates these filtered values, returning the result as the sum of odd numbers in even positions.