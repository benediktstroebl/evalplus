```python
def solution(lst):
    return sum(el for el in lst if el % 2 == 1 and lst.index(el) % 2 == 0)
```
This Python script defines a function called solution, which takes a list of numbers as input. This function iterates through the list, checking for odd numbers that appear in even positions within the list. It utilizes a summing function through a generator expression, which efficiently calculates the sum of such odd numbers within even positions and returns the result. The overall time complexity of this code is O(n), where n represents the number of elements in the input list.