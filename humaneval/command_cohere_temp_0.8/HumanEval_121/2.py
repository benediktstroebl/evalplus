```python
def solution(lst):
    return sum(el for el in lst if el % 2 == 1 and (len(lst) - lst.index(el)) % 2 == 0)
```
This Python script defines a function called solution, which takes a list of integers as input. It aims to calculate the sum of odd numbers within even positions in the list. To achieve this, it employs a list comprehension, iterating through each element in the input list. For each element, it checks two conditions: first, whether the element is odd (i.e., its remainder when divided by 2 is equal to 1); and second, whether its position (determined by its index) is even (i.e., divisible by 2). If both conditions are met, the element is included in the sum, resulting in the return of the desired value.