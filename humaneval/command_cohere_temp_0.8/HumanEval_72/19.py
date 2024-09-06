```python
def will_it_fly(q, w):
    return (sum(q) <= w) and palindrome(q)

def palindrome(q):
    return q == q[::-1]
```

The `will_it_fly()` function uses a boolean OR operation to determine if an object will fly or not. If the sum of the object's elements exceeds the maximum possible weight, it returns `False`. If the sum is within the weight limit, it checks if the list is a palindrome. If it is, it returns `True`. This function ensures that both conditions must be true for the object to have a chance of flying. 
The `palindrome()` function determines whether a list is a palindrome by comparing it to its reversed version. If the two are equal, the function returns `True`, if not, it returns `False`. This function is used to check if the nested list is balanced. 
This script ensures a straightforward approach to solving the problem statement, which checks both conditions and returns the necessary boolean values. Mentioned is a simple check for palindromes, which compares the list to its reverse. There are more efficient ways to check for palindromes, especially for nested lists, but this simple approach works and is computationally efficient.