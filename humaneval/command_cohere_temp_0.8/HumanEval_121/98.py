```python
def solution(lst):
    return sum(el for el in lst if el % 2 == 1 and (len(lst) - el + 1) % 2 == 0)
```
This Python script defines a function called solution, which takes a list of integers as input. It aims to calculate the sum of odd numbers within even positions in the list. To achieve this, it employs a list comprehension, iterating through each element (el) in the input list (lst). For each element, it checks two conditions:
1. Whether the element is odd (el % 2 == 1), and,
2. Whether its position is even (len(lst) - el + 1) % 2 == 0).

The formula (len(lst) - el + 1) is used to determine the position of an element in a list, considering indexing starts from 0. If both conditions are met, the element is included in the sum. The result is the sum of odd numbers in even positions in the list. The function omits even numbers and odd numbers in odd positions from the sum. This concise code effectively solves the challenge posed in the markdown code block.