```python
def solution(lst):
    return sum(el for el in lst if el % 2 == 1 and lst.index(el) % 2 == 0)
```
This Python script defines a function called solution, which takes a list of numbers as input. This function calculates the sum of all odd numbers present in even positions within the list. To do this, it uses a list comprehension, iterating through each element in the input list. If the element is odd and its index is even (indicating it's in an even position), it adds it to the running total, returning the result finally. 

This approach ensures odd elements in even positions are identified correctly and summed, conforming to the specified requirement.