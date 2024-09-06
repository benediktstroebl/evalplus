```python
def will_it_fly(q, w):
    return (sum(q) <= w) and check_palindrome(q)

def check_palindrome(q):
    return q == q[::-1]

# Tests
assert will_it_fly([3, 2, 3], 9) == True
assert will_it_fly([1, 2], 5) == False
assert will_it_fly([3], 5) == True
assert will_it_fly([3, 2, 3], 1) == False
```

The function `will_it_fly` uses the sum of the elements of the list `q` compared to the maximum weight `w` to determine if the object will fly or not. The condition `sum(q) <= w` ensures that the sum of the elements of `q` is less than or equal to the maximum possible weight `w`. 

The other necessary condition for the object to fly is that it needs to be balanced. The function `check_palindrome(q)` is a helper function that checks if a list `q` is a palindrome. The function returns `True` if the list is a palindrome and `False` otherwise. The function `will_it_fly` returns `True` if the object will fly, and `False` otherwise. 

This code includes a tests block that tests the `will_it_fly` function with example test cases from the problem statement. You can add more tests to this code to cover more corner cases if needed. 

If you run this code, the tests will assert that the function `will_it_fly` returns the expected outputs based on the problem statement. This way, the code demonstrates a self-contained Python script that solves the problem statement in a markdown code block.