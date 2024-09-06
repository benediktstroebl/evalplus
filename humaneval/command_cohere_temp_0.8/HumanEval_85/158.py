```python
def add(lst):
    even_odd = [el for i, el in enumerate(lst) if i % 2 == 1 and el % 2 == 0]
    return sum(even_odd)
```
This Python script defines a function called 'add()' that takes a list of integers as input. It aims to retrieve even integers occurring at odd indices within the list. To achieve this, it employs a list comprehension, iterating through each element and index of the input list. If the index is odd and the element is even, it adds the element to the 'even_odd' list. Finally, it returns the sum of the elements in the 'even_odd' list, effectively computing the desired value. 

This solution effectively addresses the problem statement and produces the expected result. For example, if the input list is `[4, 2, 6, 7]`, the function will return `2`, which is the only even integer at an odd index in the list (`2 at index 1`).