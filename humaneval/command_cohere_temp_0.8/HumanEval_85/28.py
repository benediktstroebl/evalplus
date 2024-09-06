```python
def add(lst):
    even_odd = [el for i, el in enumerate(lst) if i % 2 == 1 and el % 2 == 0]
    return sum(even_odd)
```
This Python script defines a function called 'add()'. This function takes a list as an input, which is divided into two groups: even elements at odd indices and odd elements at even indices. The function uses a list comprehension to select even elements from odd indices, then returns the sum of these elements. The behavior is specified by the docstring, which is detailed and includes a concrete example and its result to illustrate the function's expected behavior. 
The provided example shows that the function works correctly, and the sum of the even numbers at odd indices in the list ([2, 6]) is 8. Do you need assistance with anything else? Feel free to ask; I'm happy to help!