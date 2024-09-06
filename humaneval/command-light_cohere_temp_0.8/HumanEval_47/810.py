```python
def median(l):
    """Return median of elements in the list l"""
    m = []
    i = 0
    while i < len(l):
        if i == len(l) // 2:
            m.append(l[i])
        i += 1
    m.sort()
   _odd = False
    if len(m) % 2 == 1:
        m[0], m[-1] = m[-1], m[0]
        m_odd = m[1:]
    else:
        m_odd = m[::2]
    return(float(m_odd[int((len(m_odd) + 1) / 2)]))

#Example usage
 Med = median([-10, 4, 6, 1000, 10, 20])
print(Med)
 ```