```python
def solution(lst):
    return sum(el for el in lst if el % 2 == 1 and lst.index(el) % 2 == 0)
```
This Python script defines a function called solution, which takes a list of numbers as input. This function iterates through the list, checking for odd numbers that appear in even positions within the list. It utilizes the sum function to calculate the sum of odd numbers in even positions and returns the resulting value. 

The provided example use cases in the markdown code block show how the function behaves for different input lists.