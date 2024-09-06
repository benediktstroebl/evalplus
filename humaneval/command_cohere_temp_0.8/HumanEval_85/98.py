```python
def add(lst):
    even_odd = [el for i, el in enumerate(lst) if i % 2 == 1 and el % 2 == 0]
    return sum(even_odd)
```
This function uses a list comprehension to filter out even integers from the list that are located at odd indices, and then returns their sum. 

Note that the function assumes that the list contains only integers, as this is the common case for lists of 'elements'. If the list contains other data types, the function may not behave as expected. 

Let me know if you'd like to discuss further or have me make any modifications to the code to best suit your needs!