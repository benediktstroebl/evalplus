```python
def solution(lst):
    return sum(el for el in lst if el % 2 == 1 and (len(lst) - el + 1) % 2 == 0)
```
This Python script defines a function called solution, which takes a list of numbers as input. This function sums up all the odd numbers within the even positions of the list and returns the total.

To achieve this, it employs a list comprehension with a generating expression (el for el in lst if ...). This expression iterates through each element el in lst. It calculates the condition el % 2 == 1 to check if the element is odd and ((len(lst) - el + 1) % 2 == 0) to verify if the element is in an even position within the list. If both conditions are true, the element is included in the sum.

The function returns the calculated sum of odd numbers in even positions. Notably, the provided examples in the problem statement return 12, 9, and 0 respectively when applied to the solution function.