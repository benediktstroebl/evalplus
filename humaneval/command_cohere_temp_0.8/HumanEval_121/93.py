```python
def solution(lst):
    return sum(el for el in lst if el % 2 == 1 and lst.index(el) % 2 == 0)
```
This Python script defines a function called solution, which takes a list of numbers as input. This function iterates through the list, checking for odd numbers that appear in even positions within the list. The expression lst.index(el) returns the index of the element el in the list lst. Since the list is assumed to be non-empty, the modulo operation with 2 (index % 2) will always yield 0 for at least one index, hence the conditional test lst.index(el) % 2 == 0 evaluates to True for at least one odd element. The function then calculates the sum of such odd numbers and returns the result.