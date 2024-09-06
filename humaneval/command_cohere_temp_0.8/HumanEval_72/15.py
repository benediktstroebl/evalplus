```python
def will_it_fly(q, w):
    return (sum(q) <= w) and check_palindrome(q) 

def check_palindrome(q):
    return q == q[::-1]
```

The `will_it_fly` function uses a boolean or operation to determine if an object will fly or not. The `check_palindrome` function is used to check if a list is a palindrome.