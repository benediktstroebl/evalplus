```python
def add(lst):
    even_odd = []
    for i in range(len(lst)):
        if i % 2 == 1 and lst[i] % 2 == 0:
            even_odd.append(lst[i])
    return even_odd
```

This function defines an empty list 'even_odd' that stores the even integers positioned at odd indices from the input list. It efficiently solves the problem by filtering out the relevant elements using a conditional statement. The logic directly filters the even numbers sitting at odd positions and stores them in the even_odd list, which is returned thereafter. The function is concise, pragmatic, and achieves the desired outcome.