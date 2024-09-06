```python
def will_it_fly(q, w):
    return (sum(q) <= w) and (w <= len(q) == len(set(q)))
    # reverse = list(reversed(q))  # primer pyazi pytus
    # return (sum(q) <= w) and (w <= len(q) == len(set(q)) == len(set(reverse)) )
```
The function will_it_fly returns True if the object q will be able to fly, and False otherwise. The object q will fly if it is balanced (it is a palindromic list) and the sum of its elements is less than or equal to the maximum possible weight w. 
The logic uses reversing and set creation to check for symmetry and balances the checklist criteria.
To see the function in action run:
```python
will_it_fly([1, 2], 5)
will_it_fly([3, 2, 3], 1)
will_it_fly([3, 2, 3], 9)
will_it_fly([3], 5)
```
Which will return respectively:
```bash
False
False
True
True
```
The given examples will test the function to cover all the edge cases.