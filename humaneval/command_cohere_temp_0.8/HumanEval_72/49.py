```python
def will_it_fly(q, w):
    return (len(q) > 1 and 
            sum(q) <= w and 
            q == q[::-1])
```

The function will return True if the object `q` will fly according to the problem statement, and False otherwise. The function checks that the condition of being a palindromic list and the sum of its elements is less than or equal to the maximum possible weight, `w`. The additional condition of `len(q) > 1` is to prevent unbalanced single-element lists from being considered balanced. This is because the problem statement doesn't provide a clear stipulation on whether single-element lists should be considered balanced or not, and this extra condition helps to cover all possible test cases without ambiguity.