```python
def add(lst):
    even_odd = [el for i, el in enumerate(lst) if i % 2 == 1 and el % 2 == 0]
    return sum(even_odd)
```
This Python script defines a function called 'add()' that takes a list of numbers as input. It aims to collect the even numbers listed at odd indices and then adds them together to achieve a sum. A list comprehension is utilized to efficiently identify the even entries at odd indices and store them in the 'even_odd' list. After that, the sum function is used to calculate the total of the values in the 'even_odd' list. The resulting sum is then returned as the output of the function.