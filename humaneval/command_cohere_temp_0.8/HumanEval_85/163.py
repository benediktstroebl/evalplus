```python
def add(lst):
    even_odd = [el for i, el in enumerate(lst) if i % 2 == 1 and el % 2 == 0]
    return sum(even_odd)
```
This Python script defines a function named 'add', which takes a list of integers as input. It aims to retrieve even integers occurring at odd indices within the list and then calculates their sum. To achieve this, the function employs a list comprehension, iterating through each element and index of the input list. Using the condition 'i % 2 == 1 && el % 2 == 0', it filters even elements found at odd indices, storing them in the 'even_odd' list. The function then returns the sum of the even elements at odd indices. This solution aligns with the problem statement and provides the desired summation of specific even elements within the list. 

Here is a simple test to check the functionality of the add function:
```python
my_list = [4, 2, 6, 7]
print(add(my_list))
```
```bash
2
```