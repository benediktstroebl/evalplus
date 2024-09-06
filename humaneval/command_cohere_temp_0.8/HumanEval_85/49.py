```python
def add(lst):
    even_odd = [el for i, el in enumerate(lst) if i % 2 == 1 and el % 2 == 0]
    return sum(even_odd)
```
This Python script defines a function named 'add', which takes a list of integers as input. It aims to retrieve even integers occurring at odd indices within the list and then calculates their sum. To achieve this, the function employs a list comprehension, iterating through each element and index of the input list. Using the modulo operator ('%'), it identifies even elements at odd indices, assigns them to the 'even_odd' list, and finally returns the sum of these even elements. 

The function is designed to solve the specific problem mentioned in the prompt and is entirely self-contained within the provided code block. Thus, this code segment encapsulates the entire solution process within the function 'add'.