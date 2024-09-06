```python
def will_it_fly(q, w):
    return (q == q[::-1] and sum(q) <= w)
```

This function will return True if the sum of the elements in the list `q` is less than or equal to the maximum weight `w` and the list is balanced, meaning it is a palindrome. Otherwise, it returns False. This is done using a list comprehension and comparing the reversed version of the list to the original.

Here is an example of how to use this function:
```python
print(will_it_fly([3, 2, 3], 9))  # This will print True
print(will_it_fly([1, 2], 5))  # This will print False
``` 

This will return True for the first example because the sum of the list elements is less than the maximum possible weight, and it's a palindrome. The second example returns False because even though the sum of the elements is less than the maximum weight, the list is not a palindrome.