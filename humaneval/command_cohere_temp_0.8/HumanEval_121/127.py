```python
def solution(lst):
    return sum(num for num in lst if num % 2 == 1 and lst.index(num) % 2 == 0)
```
This Python script defines a function called solution, which takes a list of integers as input. It aims to calculate the sum of odd numbers present in even positions within the list. To achieve this, it employs a list comprehension, iterating through each element in the input list. For each number, it checks two conditions: first, whether the number is odd (using the modulo operator % to evaluate the remainder when divided by 2), and second, whether its index within the list is even (using the index function and checking whether the result, divided by 2, is an integer). If both conditions are met, the number is included in the sum calculated by the sum function, and the result is returned. 

This solves the problem as the function returns the sum of all the odd elements that are in even positions in the list.