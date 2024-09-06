```python
def add(lst):
    even_odd = [val for i, val in enumerate(lst) if i % 2 == 1 and val % 2 == 0]
    return sum(even_odd)
```

This function uses a list comprehension to filter out even integers from the list that are located at odd indices, and then returns their sum. 

Would you like to test this script with more examples?
Let me know if you would like me to explain any part of the solution in more detail, or provide any additional insights.