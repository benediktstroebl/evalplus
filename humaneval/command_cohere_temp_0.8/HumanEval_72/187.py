```python
def will_it_fly(q, w):
    return (sum(q) <= w) and check_palindrome(q)

def check_palindrome(q):
    return q == q[::-1]

# Tests
q1 = [1, 2]
w1 = 5
print(will_it_fly(q1, w1)) # Should print False

q2 = [3, 2, 3]
w2 = 1
print(will_it_fly(q2, w2)) # Should print False

q3 = [3, 2, 3]
w3 = 9
print(will_it_fly(q3, w3)) # Should print True

q4 = [3]
w4 = 5
print(will_it_fly(q4, w4)) # Should print True
```

In this script, the `will_it_fly` function uses the `check_palindrome` function to determine if the list `q` is a palindrome. It returns `True` if both conditions are met (the sum of elements is less than or equal to `w`, and the list is a palindrome), and `False` otherwise, following the spec above. 

The `check_palindrome` function is a helper function that determines if a given list `q` is a palindrome by comparing it to its reversed version (`q[::-1]`). If the two are equal, the function returns `True`, indicating a palindrome; otherwise, it returns `False`. 

The test suite demonstrates the function with examples from the spec, and the output is appropriately configured to print `True` or `False` based on if the object will fly according to the function. 

This solution is efficient and straightforward, using just a single pass to sum the elements of the list and another pass to compare it to its reverse.