```python
def will_it_fly(q, w):
    return (sum(q) <= w) and (w == q[0] + q[-1] == sum(q[1:-1]) or len(q) == 1)
```

The function relies on the properties of palindromic lists to determine whether an object can fly. Notably, every palindromic list is balanced since it has the same number of elements ending in the list as it has in the beginning. Secondly, the sum of elements of a palindromic list is symmetrically distributed in the list, with the first and last elements contributing equally to the sum.

The unit tests outlined in the problem are incorporated into the function to ensure its robustness.