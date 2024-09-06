```python
def median(l: list):
    """Return median of elements in the list l.
    l = [i] for i in range(len(l)) return l.median()
   _num = []
    for num in l:
        if len(l_num) == 0:
            l_num.append(num)
        else:
            if num < l_num[-1]:
                l_num.append(num)
            else:
                l_num.append(l_num[-1])
                l_num.remove(l_num[-1])
        return l_num
    l = [-10, 4, 6, 1000, 10, 20]
    return median(l)
```