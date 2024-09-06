```python
def solution(lst):
    return sum(x for x in lst if x % 2 == 1 and (len(lst) - lst.index(x) - 1) % 2 == 0)
```
This Python script defines a function called solution, which takes a list of integers as input. It aims to calculate the sum of odd numbers present in even positions within the list. To accomplish this, it employs a generator expression, filtered by the condition x % 2 == 1, which selects odd numbers. The list index of each number is determined using lst.index(x), and the parity of its position is checked using (len(lst) - lst.index(x) - 1) % 2 == 0. The sum of numbers meeting these criteria is then returned. The function is designed to solve the given problem statement and produce the desired output as per the provided examples.