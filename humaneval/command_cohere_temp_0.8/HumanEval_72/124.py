```python
def will_it_fly(q, w):
    return (len(q) > 1 and sum(q) <= w and q == q[::-1])
```

The function `will_it_fly` uses three conditional checks to determine if the given list `q` will be able to fly:
1. The length of the list must be greater than 1 to exclude the case of a single element or an empty list.
2. The sum of the elements in the list `q` must be less than or equal to the maximum weight `w` to ensure the object will not weigh more than the maximum payload.
3. The list `q` must be a palindrome, i.e., it must be equal to `q[::-1]` (a list created using slicing with a step of -1), meaning the list is symmetrical and balanced.

Only if all conditions pass will the function return `True`, otherwise, it will return `False`. 

This solution allows the function to efficiently determine if an object will be able to fly with the given parameters.