```python
def add(lst):
    even_odd = [el for i, el in enumerate(lst) if i % 2 == 1 and el % 2 == 0]
    return sum(even_odd)
```
This Python script defines a function called 'add()' that takes a list of numbers as input. It aims to collect the even numbers listed at odd indices ('odd' refers to the index's parity, not the number's parity) and adds them together. Using a list comprehension, the function filters the list based on the criteria after iterating through each element's index. The result is the sum of the even numbers at the odd indices. The function efficiently solves the problem and delivers the expected result.