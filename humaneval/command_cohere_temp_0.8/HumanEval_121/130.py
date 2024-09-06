```python
def solution(lst):
    return sum(el for el in lst if el % 2 == 1 and (len(lst) - el + 1) % 2 == 0)
```
This Python script defines a function called solution, which takes a list of numbers as input. This function calculates the sum of all odd numbers present in the list that are also in even positions. The summation is achieved using a generator expression, filtering out elements that don't meet the specified conditions. The overall time complexity of this solution is O(n), where n represents the number of elements in the input list.