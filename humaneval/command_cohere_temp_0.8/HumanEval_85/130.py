```python
def add(lst):
    even_odd = [el for i, el in enumerate(lst) if i % 2 == 1 and el % 2 == 0]
    return sum(even_odd)
```
This Python script defines a function named 'add', which takes a list of integers as input. It aims to retrieve even integers located at odd indices within the list and then calculates their sum. To achieve this, the function employs a list comprehension, iterating through each element and index of the input list. If the index is odd and the element is even, it adds the element to the 'even_odd' list. The function ultimately returns the sum of the even elements at odd indices. 

Here is an example usage of the function:
```python
input_lst = [4, 2, 6, 7]
result = add(input_lst)
print(result)
```
This will output:
```
2
```

Which proves the function operates correctly, aligning with the function's example usage provided in the initial query.