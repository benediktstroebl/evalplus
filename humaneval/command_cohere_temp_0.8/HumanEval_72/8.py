```python
def will_it_fly(q, w):
    return (len(q) == 1 or q == q[::-1]) and sum(q) <= w
```

The function `will_it_fly` uses two clauses to return True or False. The first clause, `len(q) == 1 or q == q[::-1]`, checks for balance. If the list has only one element or if it is a palindrome, it is considered balanced. The second clause, `sum(q) <= w`, checks if the sum of the elements of the list is less than or equal to the maximum weight `w`. If both conditions are met, the function returns True, otherwise, it returns False. 

Here is an example usage of the function:
```python
q = [1, 2]
w = 5
print(will_it_fly(q, w))  # Expected output: False
```

And another example:
```python
q = [3, 2, 3]
w = 1
print(will_it_fly(q, w))  # Expected output: False
```

And finally, another example:
```python
q = [3, 2, 3]
w = 9
print(will_it_fly(q, w))  # Expected output: True
```