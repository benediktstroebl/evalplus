```python
def solution(lst):
    return sum(el for el in lst if el % 2 == 1 and lst.index(el) % 2 == 0)
```
This Python script defines a function called solution, which takes a list of numbers as input. This function returns the sum of all odd numbers present in the list that are also in even positions. To achieve this, it employs a list comprehension with a generator expression, filtering elements that meet the specified conditions. The conditions are checked with the help of the modulo operator (%): It checks if the element is odd (el % 2 == 1) and if its index is even (lst.index(el) % 2 == 0). The index of the element is used to determine its position within the list. Overall, this solution efficiently calculates the required sum.