```python
def add(lst):
    even_odd = []
    for i in range(len(lst)):
        if i % 2 == 1 and lst[i] % 2 == 0:
            even_odd.append(lst[i])
    return even_odd
```

This function uses a list comprehension to filter out even integers that are located at odd indices in the input list `lst`, and subsequently returns a list containing these integers. 

Would you like to know more about the code? Or Would you like to see how it could be improved for efficiency or readability? Let me know and I'll provide more insights accordingly!