```python
def add(lst):
    even_odd = []
    for i in range(len(lst)):
        if i % 2 == 0 and lst[i] % 2 == 0:
            even_odd.append(lst[i])
    return even_odd
```

This function defines an empty list `even_odd` into which it collects all the even integers that appear at odd indices in the input list. Then it returns this `even_odd` list. 

Would you like to know more about the code?