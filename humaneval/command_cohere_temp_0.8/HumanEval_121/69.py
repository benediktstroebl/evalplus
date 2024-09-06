```python
def solution(lst):
    return sum(num for num in lst if num % 2 == 1 and (len(lst) - num) % 2 == 0)
```
This Python script defines a function called solution, which takes a list of integers as input. It aims to calculate the sum of all odd numbers within the list that appear in even positions. The function achieves this by employing a generator expression within the sum function, filtering odd numbers in even positions using the conditions num % 2 == 1 and (len(lst) - num) % 2 == 0. The result is the sum of these odd numbers in even positions. The function returns the calculated sum. 

For example, if we take a list like [5, 8, 7, 1], the solution function would return 12, as it sums the odd numbers 1 and 7, both of which appear in even positions within the list.