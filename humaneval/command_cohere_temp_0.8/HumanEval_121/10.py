```python
def solution(lst):
    return sum(el for el in lst if el % 2 == 1 and lst.index(el) % 2 == 0)
```
This Python script defines a function called solution, which takes a list lst as input. It aims to calculate the sum of odd integers present in even positions within the list. To do this, it employs a list comprehension, iterating through each element el in lst. Using the modulo operator % 2, it identifies elements that are odd (el % 2 == 1). Additionally, it checks if the index of the element (obtained using lst.index(el)) is even (index % 2 == 0). This ensures that the element is in an even position within the list. If both conditions are met, the element is included in the sum, which is then returned as the function's result.