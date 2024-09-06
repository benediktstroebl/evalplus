```python
def add(lst):
    even_odd = [el for i, el in enumerate(lst) if i % 2 == 1 and el % 2 == 0]
    return sum(even_odd)
```
This Python script defines a function named 'add', which takes a list of integers as input. It aims to accumulate and return the sum of even integers present at odd indices in the input list. To achieve this, the function employs a list comprehension, which iterates through each element and index of the input list using the enumerate function. It filters elements that satisfy two conditions: (1) the index's parity is odd (i.e., index % 2 == 1), and (2) the element's parity is even (i.e., el % 2 == 0). The filtered elements are collected into the 'even_odd' list, and the function then returns the sum of these elements, providing the total of the even integers located at odd indices in the input list.