```python
def solution(lst):
    return sum(el for el in lst if el % 2 == 1 and lst.index(el) % 2 == 0)
```
This Python script defines a function called solution, which takes a list of numbers as input. This function calculates the sum of all odd numbers present in even positions in the list. To accomplish this, it employs a list comprehension with a conditional statement. The conditional statement checks if each element in the list is odd (el % 2 == 1) and whether its index is even (lst.index(el) % 2 == 0). The sum function then adds up the values that satisfy both conditions. The resulting output is the sum of odd elements situated in even positions within the provided list.