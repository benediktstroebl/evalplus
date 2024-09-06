```python
def add(lst):
    even_odd = [el for i, el in enumerate(lst) if i % 2 == 1 and el % 2 == 0]
    return sum(even_odd)
```
This function uses a list comprehension to filter out even elements at odd indices from the input list and then uses the sum function to add these numbers. 

Here is a usage example of the function for the problem example:
```python
print(add([4, 2, 6, 7]))
```
Which prints out the expected output of 2, formed by the even elements at odd indices: 2 and 6. 

This solution can be optimized further using a single pass and without creating a new list using the filtering capability of list comprehension. 

Here is an optimized version of the code:
```python
def add(lst):
    return sum(el for el in lst if el % 2 == 0 and lst.index(el) % 2 == 1)
```
In this version, the index of the element is checked instead of the index of the list comprehension. This is a more efficient approach as the list is not needed for filtering.