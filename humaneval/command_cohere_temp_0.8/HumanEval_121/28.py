```python
def solution(lst):
    return sum(x for x in lst if x % 2 == 1 and (len(lst) - lst.index(x) - 1) % 2 == 0)
```
This Python script defines a function called solution, which takes a list of integers as input. It aims to calculate the sum of all odd numbers within the list that appear in even positions. The function achieves this by employing a generator expression within the sum function, filtering elements that meet the condition of being odd (x % 2 == 1) and appearing in even positions ( indexes which are divisible by 2). The result is the sum of these odd numbers in even positions. The overall time complexity of this code is O(n), where n represents the size of the input list.