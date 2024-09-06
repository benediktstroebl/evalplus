```python
def add(lst):
    even_odd = [val for i, val in enumerate(lst) if i % 2 == 1 and val % 2 == 0]
    return sum(even_odd)
```
This Python script defines a function called 'add()' that takes a list of numbers as input. It aims to accumulate and return the sum of even numbers present at odd indices in the input list. To achieve this, it employs a list comprehension, iterating through each element and index of the input list. If the current index is odd and the corresponding value is even, it adds the value to the 'even_odd' list. The final result is the sum of odd-indexed even numbers, returned by the function.