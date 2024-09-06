```python
def add(lst):
    even_odd = [el for i, el in enumerate(lst) if i % 2 == 1 and el % 2 == 0]
    return sum(even_odd)
```
This Python script defines a function named 'add', which takes a list of integers as input. It aims to accumulate and return the sum of even integers present at odd indices in the given list. To achieve this, the function employs a list comprehension, which iterates through each element and index of the input list. If the current index is odd and the corresponding element is even, it adds the element to the 'even_odd' list. The final sum of the odd-indexed even numbers is then returned as the function's result, as explained in the problem statement and exemplified in the provided example test case.