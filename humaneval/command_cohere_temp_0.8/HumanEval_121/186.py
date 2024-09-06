```python
def solution(lst):
    return sum(el for el in lst if el % 2 == 1 and lst.index(el) % 2 == 0)
```
This Python script defines a function called solution, which takes a list lst as input. It aims to calculate the sum of odd numbers present in even positions within the list. To do this, it employs a list comprehension within the sum function. For each element el in the input list, the condition el % 2 == 1 checks if the element is odd, and lst.index(el) % 2 == 0 checks if the element's index is even. The sum function then computes the sum of all elements that satisfy both conditions. The result is the desired sum of odd numbers in even positions within the list.