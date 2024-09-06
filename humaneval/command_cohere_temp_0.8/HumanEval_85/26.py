```python
def add(lst):
    even_odd = [el for i, el in enumerate(lst) if i % 2 == 1 and el % 2 == 0]
    return sum(even_odd)
```
This Python script defines a function called 'add()' that takes a list of numbers as an input. It aims to accumulate and return the sum of even numbers present at odd indices in the given list. To achieve this, it uses a list comprehension, iterating through each element and index in the input list. If the current element is even and it's at an odd index (determined by the modulo operation), it adds the element to the 'even_odd' list. Finally, the function returns the sum of the accumulated even numbers, providing a numeric result as specified in the problem statement.