```python
def will_it_fly(q, w):
    return (sum(q) <= w) and check_palindrome(q) 

def check_palindrome(q):
    return q == q[::-1]
```

The `will_it_fly` function uses a palindrome checker to determine if the list is balanced. The `check_palindrome` function is used to determine if the list is symmetrical. The sum of the list is compared to the maximum weight, and if both conditions are met, the function returns `True`. If either condition is not met, the function returns `False`. 

This solution utilizes only a basic comprehension of Python and uses a straightforward approach to solving the problem. Feel free to further customize the code to your liking or add more test cases to ensure its reliability. Let me know if you'd like me to explain any part of the solution in more detail.