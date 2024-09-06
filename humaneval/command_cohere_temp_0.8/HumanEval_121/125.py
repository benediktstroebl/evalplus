```python
def solution(lst):
    return sum(el for el in lst if el % 2 == 1 and (len(lst) - el + 1) % 2 == 0)
```
This Python script defines a function called solution, which takes a list of numbers as input. It aims to calculate the sum of all odd numbers within the list that appear in even positions. To accomplish this, it employs a list comprehension, iterating through each element in the input list. For each element, it checks two conditions: first, whether the element is odd (el % 2 == 1), and second, whether its position in the list is even (len(lst) - el + 1) % 2 == 0). If both conditions are met, the element is included in the sum, and the result is returned. The function operates without affecting the original list, providing a concise and efficient solution to the problem.