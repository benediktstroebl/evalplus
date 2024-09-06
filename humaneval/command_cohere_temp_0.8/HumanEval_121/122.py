```python
def solution(lst):
    return sum(el for el in lst if el % 2 == 1 and lst.index(el) % 2 == 0)
```
This Python script defines a function called solution, which takes a list lst as input. It aims to calculate the sum of odd numbers present in even positions within the list. To do this, it employs a list comprehension, iterating through each element el in lst. Within the list comprehension, it checks if el is an odd number (el % 2 == 1) and if it occupies an even position in the list (indexed with lst.index(el) % 2 == 0). This ensures it sums only the odd numbers in even positions, regardless of the list's length or content. The result is the sum of these odd numbers meeting the criteria.