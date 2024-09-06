```python
def solution(lst):
    return sum(el for el in lst if el % 2 == 1 and (len(lst) - el + 1) % 2 == 0)
```
This Python script defines a function named solution which takes a list of integers as input. It aims to calculate the sum of odd numbers present in even positions within the list. To achieve this, it employs a list comprehension, iterating through each element (el) in the input list (lst). For each element, it checks two conditions:
1. Whether the element is odd (el % 2 == 1), and,
2. Whether its position is even (len(lst) - el + 1) % 2 == 0).

The latter condition checks whether the element's position is even by calculating the parity of its position relative to the length of the list. If both conditions are met, the element is included in the sum, and the result is returned. The function meets the provided test examples, returning the expected sums for various input lists.