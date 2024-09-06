```python
def add(lst):
    even_odd = [val for i, val in enumerate(lst) if i % 2 == 1 and val % 2 == 0]
    return sum(even_odd)
```

This function uses a list comprehension to filter out even integers from the list that are located at odd indices, and then returns their sum. The problem scenario provided exhibits this scenario with an example list of `[4, 2, 6, 7]`, and the function returns `2`, which is indeed the sum of the even integers at odd indices in this list: `2` and `6`. 

Do you need assistance with anything else? Feel free to ask, and I shall assist you to the best of my abilities!