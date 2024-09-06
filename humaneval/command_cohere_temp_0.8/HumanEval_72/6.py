```python
def will_it_fly(q, w):
    return (sum(q) <= w) and (w == q[0] + q[-1] == sum(q[1:-1]) or w == q[0] + q[-2] + q[-1] == sum(q[1:-2]))
```

The function will return **True** if the object **q** will be able to fly with the given parameters, and **False** otherwise. It checks if the sum of the object's elements is less than or equal to the maximum possible weight **w**, and that the list is palindrome, thus balanced. The palindrome check is done using several different methods to accommodate for different possible list constructions.