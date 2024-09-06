```python
def add(lst):
    even_odd = [el for i, el in enumerate(lst) if i % 2 == 1 and el % 2 == 0]
    return sum(even_odd)
```
This Python script defines a function named 'add', which takes a list of integers as input. It aims to retrieve even integers occurring at odd indices within the list and then calculates their sum. To achieve this, the function employs a list comprehension, iterating through each element and index of the input list. Using the modulo operator ('%'), it identifies even elements at odd indices, assigns them to the 'even_odd' list, and finally returns the sum of these even elements. 

The function is self-contained, meaning it does not rely on any external variables or assumptions, and can be executed independently. 
The behavior of the 'add' function is exemplified through tests that verify both the summation of even elements at odd indices and the appropriate handling of lists without any such elements.