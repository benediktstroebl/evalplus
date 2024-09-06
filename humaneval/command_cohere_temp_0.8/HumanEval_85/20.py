```python
def add(lst):
    even_odd = [el for i, el in enumerate(lst) if i % 2 == 1 and el % 2 == 0]
    return sum(even_odd)
```
This function uses a list comprehension to filter out even integers from the list that are located at odd indices, and then returns their sum. The problem scenario provided examples and expected results, but the solution does not include them as they are not necessary to understand the code. I left it out for brevity. Let me know if you need anything else!