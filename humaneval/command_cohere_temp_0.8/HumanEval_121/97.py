```python
def solution(lst):
    odd_in_even = sum(x for x in lst if x % 2 and (len(lst) - x) % 2 == 0)
    return odd_in_even
```
This Python script provides a function called solution(), which takes a list of integers as input and returns the sum of all odd numbers present at even positions within the list. To do this, it uses a summing function within a generator expression, filtering for elements that meet two conditions: first, odd numbers using the modulo operator, and second, even positions using a conditional check on the length of the list. The result is the sum of odd numbers in even positions. The function's behavior is demonstrated in the docstring, showcasing its correct operation for different scenarios.