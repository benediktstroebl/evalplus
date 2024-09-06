```python
def solution(lst):
    return sum(el for el in lst if el % 2 == 1 and (len(lst) - el + 1) % 2 == 0)
```
This Python script defines a function called solution, which takes a list of integers as input. It aims to calculate the sum of odd numbers within even positions in the list. To achieve this, it employs a list comprehension, iterating through each element (el) in the input list (lst). For each element, it checks two conditions:
1. OddElement: It checks if the element is odd, i.e., if its remainder when divided by 2 is equal to 1 (el % 2 == 1).
2. EvenPosition: It checks if the element's position in the list is even. To determine this, it calculates (len(lst) - el + 1) modulo 2, which represents the position of the current element in the list. If this result is equal to 0 (i.e., even position), it satisfies this condition.

Only when both conditions are met, the element is included in the sum, and ultimately returned as the result of the function. This approach ensures the function calculates the requested sum of odd numbers in even positions in the list.