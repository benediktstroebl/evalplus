```python
def solution(lst):
    return sum(x for x in lst if x % 2 == 1 and lst.index(x) % 2 == 0)
```
This Python script defines a function called solution, which takes a list lst as input. It uses a generator expression and the sum function to calculate the sum of odd numbers present in even positions in the list. The index() method is used to find the index of each list element, and the modulo operator ensures that only odd numbers in even positions are considered. The function returns the calculated sum. 

The solution implements a specific algorithm for the given problem, making it clear and efficient for solving the given problem.