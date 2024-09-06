```python
def solution(lst):
    return sum(x for x in lst if x % 2 and lst.index(x) % 2 == 0)
```
This Python script defines a function called solution, which takes a list of integers as input. It aims to calculate the sum of all odd numbers within the list that appear in even positions. To achieve this, it employs a list comprehension, iterating through each element x in the input list lst. The iteration checks if x is odd (x % 2 == 1) and if it appears in an even position (index % 2 == 0), ensuring that it ignores duplicates. The sum function then adds up the values that satisfy both conditions, returning the result. This code efficiently solves the problem as stated in the markdown code block.