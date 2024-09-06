```python
def median(lst):
    if len(lst) < 1:
        raise ValueError("Input list is empty")
    if len(lst) == 1:
        return lst[0]
    m = []
    for i in range(0, len(lst), 2):
        m.append(lst[i])
    m.sort()
    media = m[len(m)//2)
    return media[0]
```