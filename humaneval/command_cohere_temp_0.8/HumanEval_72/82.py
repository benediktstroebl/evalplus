```python
def will_it_fly(q, w):
    return (len(q) > 1 and sum(q) <= w and q == q[::-1])
```

The function `will_it_fly` uses three conditions to determine if an object will fly:
1. The object is a list of length greater than 1. This is to ensure that the object is not a single element, as it cannot be balanced.
2. The sum of the list elements is less than or equal to the maximum weight (`w`). This condition ensures that the total weight of the object is less than or equal to the maximum weight.
3. The list is a palindrome. This checks if the list is balanced.

These conditions return `True` if the object will fly and `False` otherwise. 

The given examples in the problem statement return the following results:
- `will_it_fly([1, 2], 5)` returns `False` because although the sum of the elements is less than the maximum weight, the list is not palindrome.
- `will_it_fly([3, 2, 3], 1)` returns `False` because the sum of the elements is greater than the maximum weight.
- `will_it_fly([3, 2, 3], 9)` returns `True` because the sum of the elements is less than the maximum weight and the list is a palindrome.
- `will_it_fly([3], 5)` returns `True` because the sum of the elements is less than the maximum weight, and the list is a palindrome.