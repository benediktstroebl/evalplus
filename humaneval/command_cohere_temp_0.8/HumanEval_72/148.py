```python
def will_it_fly(q, w):
    return (sum(q) <= w) and (w >= max(q)) and palindrome(q)

def palindrome(q):
    return q == q[::-1]
```

The function will_it_fly checks if the sum of elements in the list q is less than or equal to the maximum possible weight w, that the elements of q are balanced (i.e., it's a palindrome), and returns True if so; otherwise, it returns False. The palindrome function is used to check if the list q is a palindrome by comparing it to its reverse q[::-1].