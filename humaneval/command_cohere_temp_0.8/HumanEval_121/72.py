```python
def solution(lst):
    return sum(el for el in lst if el % 2 == 1 and lst.index(el) % 2 == 0)
```
This Python script defines a function called solution, which takes a list of numbers as input. This function calculates the sum of all odd numbers present in even positions within the list. To accomplish this, it employs a list comprehension with a conditional statement. The sum function is used in the list comprehension to compute the sum of values that meet the condition. Notably, the index of the list element is calculated using the index function, and the modulus operator is used to ascertain whether the element is in an even position. The function returns the calculated sum of odd numbers in even positions.