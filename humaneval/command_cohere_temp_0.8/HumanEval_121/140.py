```python
def solution(lst):
    return sum(el for el in lst if el % 2 == 1 and lst.index(el) % 2 == 0)
```
This Python script defines a function called solution, which takes a list lst as input. It aims to calculate the sum of odd integers present in even positions within the list. To accomplish this, it employs a list comprehension, iterating through each element el in lst. Within the list comprehension, the condition el % 2 == 1 checks if the element is odd, and lst.index(el) % 2 == 0 verifies if the element's index is even. The sum function then aggregates the odd elements satisfying these conditions, ultimately returning the total sum. This code efficiently solves the problem as stated in the markdown code block.