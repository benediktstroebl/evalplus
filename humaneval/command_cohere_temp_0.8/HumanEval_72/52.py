```python
def will_it_fly(q, w):
    return (sum(q) <= w) and palindromic_list(q)

def palindromic_list(l):
    return l == l[::-1]
```

The `will_it_fly` function uses a boolean OR operation to determine if an object will fly or not. If the sum of the object's elements exceeds the maximum possible weight, it returns `False`, regardless of whether the list is balanced or not. Similarly, if the list is not balanced (not a palindrome), it returns `False`, regardless of the sum of its elements. The function will return `True` only if the sum of elements is less than or equal to the maximumorch possible weight and the list is balanced.

The `palindromic_list` function determines whether a list is a palindrome by comparing it to its reversed version. If the two are identical, the function returns `True`; otherwise, it returns `False`. This function specifically checks the symmetry of the list, ignoring the weight of the elements.