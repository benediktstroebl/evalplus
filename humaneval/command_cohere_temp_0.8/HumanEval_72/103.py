```python
def will_it_fly(q, w):
    return (len(q) > 1 and sum(q) <= w and q == q[::-1])
```

The function `will_it_fly` uses three conditional checks to determine if the given list `q` will be able to fly:
1. The length of the list `q` is greater than 1 to ensure it is not a single element or empty, preventing false positives on single digits or empty lists which would be balanced but have no weight requirement to meet.
2. The sum of the elements in list `q` is less than or equal to the maximum weight `w` it can have. This ensures that the weight requirement is met or exceeded, so the object will not be too heavy to lift. 
3. The list `q` is symmetric (palindromic), meaning it is balanced. The list is compared to its reversed version using the slicing operator `[:]-1` to create an reversed copy of the list, and the equality is checked to determine if it is symmetric. 

Each of these checks ensures a necessary condition for the object to be able to fly. If all conditions return True, the function will return True, otherwise it will return False. 

This solution tests each of these conditions and returns True if the object will be able to fly, and False otherwise.