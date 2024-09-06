```python
def add(lst):
    even_odd = [el for i, el in enumerate(lst) if i % 2 == 1 and el % 2 == 0]
    return sum(even_odd)
```
This Python script defines a function called 'add()'. This function takes a list as input and aims to calculate the sum of even integers present at odd indices in the list. Using a list comprehension, it sifts through the list, identifying elements at odd indices that are even. These qualifying elements are accumulated and returned as the sum. 

For better clarity, here is an example usage of the function:
```python
result = add([4, 2, 6, 7])
print(result)
> 2
```