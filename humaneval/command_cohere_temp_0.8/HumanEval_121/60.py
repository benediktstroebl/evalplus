```python
def solution(lst):
    return sum(el for el in lst if el % 2 == 1 and (len(lst) - el + 1) % 2 == 0)
```
This Python script defines a function named solution which takes a list of numbers as an input. This function is designed to calculate the sum of all odd numbers within the even positions of the list. To achieve this, it employs a list comprehension, iterating through each element in the input list. For each element, it checks two conditions: first, whether the element is odd (i.e., its remainder when divided by 2 is equal to 1), and second, whether its position within the list is even (i.e., its index is divisible by 2). If both conditions are met, the element is included in the sum, resulting in the return of the total odd value at even positions.