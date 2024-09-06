```python
def solution(lst):
    return sum(x for x in lst if x % 2 and lst.index(x) % 2 == 0)
```
This Python script defines a function called solution, which takes a list lst as input. It employs a conditional expression, `x for x in lst if x % 2 and lst.index(x) % 2 == 0`, to iterate through each element x in the input list. It filters elements that are odd (x % 2 == 1) and located in an even position (index() % 2 == 0). The sum of these filtered elements is then returned as the result, satisfying the requirement of summing the odd elements in even positions in the input list.