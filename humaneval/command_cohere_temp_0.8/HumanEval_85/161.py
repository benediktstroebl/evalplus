```python
def add(lst):
    even_odd = [el for i, el in enumerate(lst) if i % 2 == 1 and el % 2 == 0]
    return sum(even_odd)
```
This Python script defines a function named 'add', which takes a list of integers as input. It aims to retrieve even integers positioned at odd indices within the list and then calculates their sum. To achieve this, it employs a list comprehension, iterating through each element and index of the provided list using the enumerate function. When the index is odd (i % 2 == 1) and the element is even (el % 2 == 0), the element is added to the even_odd list. The function subsequently returns the sum of the even elements at odd indices, providing the total of the targeted values within the list.