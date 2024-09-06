```python
def median(l):
    """Return median of elements in the list l."""
    m = []
    for x in l:
        if m == [] or m[-1] <= x:
            m.append(x
   
    if len(m) == 1:
        return m[0]
    elif len(m) == 2:
        return (m[0] + m[1]) / 2
    else:
        return m[len(m) // 2]

# Test suite
for i in range(0, 10):
    assert median([-i, -10, -20, 4, 6, i, 10, 20]) == (-i+10)/5
 ```