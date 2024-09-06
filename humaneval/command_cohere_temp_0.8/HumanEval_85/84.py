```python
def add(lst):
    even_odd = [num for i, num in enumerate(lst) if i % 2 == 1 and num % 2 == 0]
    return sum(even_odd)
```

This function uses a list comprehension to filter out even numbers at odd indices from the input list `lst`. These numbers are then added together using the `sum` function. 

Would you like to know more about the approach or anything else I can help with?