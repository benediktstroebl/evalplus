```python
def solution(lst):
    return sum(el for el in lst if el % 2 == 1 and lst.index(el) % 2 == 0)
```
This Python script defines a function called solution, which takes a list of numbers as input. This function calculates the sum of all odd numbers present in even positions in the list. To achieve this, it employs a list comprehension with a conditional statement. The conditional statement `el % 2 == 1` checks if each list element `el` is odd, and `lst.index(el) % 2 == 0` verifies if the element's index is even. The sum operation then computes the total of numbers satisfying these conditions. The function returns the resulting sum. 

This solution ensures that only odd numbers in even positions are selected, as dictated by the problem statement.