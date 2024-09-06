```python
def factorize(n): 
    factors = [] 
    while n > 1: 
        d = divmod(n, 2) 
        if d[1] == 0: 
            factors.append(2) 
            n = n // 2 
        else: 
            m = 3
            while m <= int(n ** 0.5): 
                d = divmod(n, m)
                if d[1] == 0: 
                    factors.append(m) 
                    n = n // m 
                m += 1 
    return factors
 ```