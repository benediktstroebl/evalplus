```python
def add(lst):
    even_odd = [el for i, el in enumerate(lst) if i % 2 == 1 and el % 2 == 0]
    return sum(even_odd)
```
This Python script defines a function called 'add()' that takes a list of numbers as input. It aims to collect the even integers present at odd indices of the list using a list comprehension. The collected even integers are then added together using the 'sum()' function, which returns the total of these even elements at odd indices.