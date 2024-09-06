```python
def add(lst):
    even_odd = [el for i, el in enumerate(lst) if i % 2 == 1 and el % 2 == 0]
    return sum(even_odd)
```
This Python script defines a function named 'add', which takes a list of integers as input. It aims to collect the even integers present at odd indices in the list and compute their sum. To achieve this, it uses a list comprehension, iterating through each element and index of the input list. If the index is odd (i.e., `i % 2 == 1`) and the element is even (`el % 2 == 0`), it adds the element to the `even_odd` list. Finally, the function returns the sum of the elements in the `even_odd` list, which effectively captures the even integers present at odd indices in the input list. 

The function effectively solves the problem statement and can be used as a standalone Python function to solve the specified problem.