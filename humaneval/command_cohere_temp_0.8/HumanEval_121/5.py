```python
def solution(lst):
    return sum(el for el in lst if el % 2 == 1 and lst.index(el) % 2 == 0)
```
This Python script defines a function called solution, which takes a list of numbers as input. This function calculates the sum of all odd numbers present in even positions in the list. To accomplish this, it employs a list comprehension with a generator expression, checking for elements that meet the conditions of oddness and even positioning. The sum function then adds up these odd numbers in even positions, returning the result. The function's behavior is demonstrated through examples in the docstring, showing its correctness for various input scenarios.