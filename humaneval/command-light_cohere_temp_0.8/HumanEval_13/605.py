```python
def greatest_common_divisor(a, b):
    if not a or not b:
        return 0

    # prime factorization using factor() method 
    # and checking the maximum power of each factor 
    # that occurs in both numbers 
    pfs = []
    while a > 0:
        p = a % b
        if p == 0:
            pfs.append(b)
            a = 1
        a = a // p
    b = b // p
    pfs.append(a)

    # checking the maximum power of each factor 
    m = 0
    for p in pfs:
        if m < p:
            break
        m += 1

    # checking if any common divisor is greater than m 
    for p in pfs:
        if m <= p:
            return p

    return -1
```