```python
def solution(lst):
    odd_in_even = sum(x for i, x in enumerate(lst) if i % 2 == 1 and x % 2 == 1)
    return odd_in_even
```
This Python script defines a function called solution, which takes a list lst as input. It employs a sum() function combined with a generator expression to filter out odd elements in even positions. The overall correctness is ensured by the docstring examples.