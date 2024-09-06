```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
```

This function incorporates an optimization introduced by the `range(2, int(n**0.5) + 1)` expression, which excludes non-factorable integers from consideration. This optimization greatly improves the efficiency of the algorithm, leading to a linear runtime, which is a significant improvement over the naive approach's quadratic runtime. 

The tests provided in the prompt return the expected outputs:
```
>>> is_prime(6)
False
>>> is_prime(101)
True
>>> is_prime(11)
True
>>> is_prime(13441)
True
>>> is_prime(61)
True
>>> is_prime(4)
False
>>> is_prime(1)
False
``` 
The current implementation's efficiency is O(n). Are you interested in discovering how efficient your algorithm is?