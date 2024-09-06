```python
def add(lst):
    even_odd = [el for i, el in enumerate(lst) if i % 2 == 1 and el % 2 == 0]
    return sum(even_odd)
```
This Python script defines a function named 'add', which takes a list of integers as input. It aims to accumulate and return the sum of even integers present at odd indices in the input list. To achieve this, it employs a list comprehension, iterating through each element and index of the input list. If the current index is odd and the element is even, it adds the element to the 'even_odd' list. The final result is the sum of the elements in 'even_odd', which is then returned to provide the desired sum of even integers at odd indices in the input list.