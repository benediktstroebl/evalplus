```python
def solution(lst):
    return sum(el for el in lst if el % 2 == 1 and lst.index(el) % 2 == 0)
```
This Python script defines a function called solution, which takes a list of integers as input. It aims to calculate the sum of all odd numbers within the list that appear in even positions. To accomplish this, it employs a list comprehension, iterating through each element in the input list. For each element, it checks if the element is odd and if its position in the list is even (indexing starts from 0). If both conditions are met, the element is included in the sum, and the total is returned as the function's result. The function's output is a sum of odd numbers in even positions, as specified in the problem statement.