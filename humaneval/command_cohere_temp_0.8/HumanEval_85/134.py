```python
def add(lst):
    even_odd = [el for i, el in enumerate(lst) if i % 2 == 1 and el % 2 == 0]
    return sum(even_odd)
```
This Python script defines a function called 'add()' that takes a list of numbers as input. It aims to collect the even numbers listed at odd indices and then adds them together to achieve a sum. This behavior is exemplified in the function's example execution, where it calculates the sum of the even numbers at odd indices in the input list and appropriately returns the expected result.