```python
def solution(lst):
    odd_in_even = sum(x for i, x in enumerate(lst) if i % 2 == 1 and x % 2 == 1)
    return odd_in_even
```
This Python script provides a function called solution(), which takes a list of integers as input and returns the sum of all odd numbers present in even positions in the list. To achieve this, it employs a sum() function and a generator expression to filter out odd numbers in even positions, summing them up into the odd_in_even variable. The result is the total of odd numbers in even list positions.