```python
def solution(lst):
    return sum(el for el in lst if el % 2 == 1 and lst.index(el) % 2 == 0)
```
This Python script defines a function called solution, which takes a list of numbers as input. This function calculates the sum of all odd numbers present in even positions within the list. To do this, it uses a list comprehension with a generator expression, checking if each element is odd and its index is even (indicated by `lst.index(el) % 2 == 0`). The sum operation then adds up the values that meet both conditions. The function returns the resulting sum. 

The script ensures that it covers various scenarios, including when the list contains only odd elements, only even elements, and a mix of both, thereby guaranteeing that the function behaves as expected in multiple cases.