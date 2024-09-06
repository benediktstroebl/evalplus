```python
def add(lst):
    even_odd = [el for i, el in enumerate(lst) if i % 2 == 1 and el % 2 == 0]
    return sum(even_odd)
```
This Python script defines a function called 'add()' that takes a list of numbers as input. It aims to accumulate and return the sum of even numbers present at odd indices in the list. To achieve this, it employs a list comprehension, iterating through each element and index in the input list. If the current element is even and it occupies an odd index (determined by the expression 'i % 2 == 1'), it gets included in the 'even_odd' list. Finally, the function returns the sum of the numbers in the 'even_odd' list, which effectively addresses the task of adding even elements at odd indices in the list.