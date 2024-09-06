```python
def add(lst):
    even_odd = [el for i, el in enumerate(lst) if i % 2 == 1 and el % 2 == 0]
    return sum(even_odd)
```
This Python script defines a function called 'add()' that takes a list of integers as input. It aims to accumulate and return the sum of even integers present at odd indices in the input list. To achieve this, it employs a list comprehension, iterating through each element and index in the input list. If the current index is odd and the element is even, it adds the element to the 'even_odd' list. The final sum of the accumulated even integers is then returned as the function's result. 

The function efficiently solves the problem and provides the desired sum of even elements at odd indices in the given list.