```python
def solution(lst):
    return sum(el for el in lst if el % 2 == 1 and lst.index(el) % 2 == 0)
```
This Python script defines a function called solution, which takes a list lst as input. It employs a list comprehension to iterate through each element el in the input list. It seeks elements that satisfy two conditions: first, it checks if the element is odd (i.e., el % 2 == 1), and second, it verifies if the element's index (determined using lst.index(el)) is even (i.e., index % 2 == 0). The sum function calculates the sum of all elements that meet both conditions. This approach effectively solves the given problem, returning the sum of odd elements positioned in even indices within the list.