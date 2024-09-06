```python
def will_it_fly(q, w):
    return (len(q) > 1 and 
            sum(q) <= w and 
            q == q[::-1])
```

The function will return True if the object q will be able to fly under the given conditions, and False otherwise. The conditions being that the object must be a palindrome (balanced) and the sum of its elements must be less than or equal to the maximum possible weight w. If the object is not balanced or the sum of its elements exceeds the weight, it will not be able to fly.  The examples provided in the prompt should output accordingly based on these conditions.