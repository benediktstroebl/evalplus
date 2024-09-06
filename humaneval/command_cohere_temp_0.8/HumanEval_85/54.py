```python
def add(lst):
    even_odd = [el for i, el in enumerate(lst) if i % 2 == 1 and el % 2 == 0]
    return sum(even_odd)
```
This Python script defines a function called 'add()' that takes a list of integers as input. It aims to collect the even integers appearing at odd indices of the list into a separate list called 'even_odd'. Then it returns the sum of all elements in the 'even_odd' list. The self-contained nature of the code is emphasized by the absence of external dependencies or required arguments.