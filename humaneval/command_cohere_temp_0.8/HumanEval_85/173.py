```python
def add(lst):
    even_odd = [el for i, el in enumerate(lst) if i % 2 == 1 and el % 2 == 0]
    return sum(even_odd)
```
This Python script defines a function named 'add', which takes a list of integers as input. It aims to retrieve even integers located at odd indices within the list and then calculate their sum. To achieve this, the function employs a list comprehension, iterating through each element and index of the input list. If the index is odd and the element is even, it adds the element to the 'even_odd' list. The function then returns the sum of the elements in 'even_odd', providing a total of the odd-indexed even numbers in the original list.