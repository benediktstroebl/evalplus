```python
def add(lst):
    even_odd = [el for i, el in enumerate(lst) if i % 2 == 1 and el % 2 == 0]
    return sum(even_odd)
```
This Python script defines a function called 'add()' that takes a list of numbers as an input. It aims to accumulate and return the sum of even numbers present at odd indices in the list. To achieve this, it uses a list comprehension that iterates through the indices and elements of the input list simultaneously. For each element at an odd index (i.e., when `i % 2 == 1`), it includes the element in the 'even_odd' list only if it is divisible by 2 (i.e., `el % 2 == 0`). Finally, the function returns the sum of the elements in the 'even_odd' list, resulting in the desired output.