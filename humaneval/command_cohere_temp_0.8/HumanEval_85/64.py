```python
def add(lst):
    even_odd = [el for i, el in enumerate(lst) if i % 2 == 1 and el % 2 == 0]
    return sum(even_odd)
```
This Python script defines a function named 'add'. This function takes a list as input and works as follows:
- It uses a list comprehension to traverse the list `lst`.
- For each element `el` at an odd index (where `i % 2 == 1`), it checks if this element is even (using `el % 2 == 0`).
- If the condition is true, the element is added to the `even_odd` list.
- Finally, the function returns the sum of all the even elements at odd indices in the input list, as requested by the problem statement.