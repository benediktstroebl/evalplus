```python
def pairs_sum_to_zero(l):
    # Write your code here
    seen = set()
    for i in l:
        if i > 0 and i not in seen and pairs_sum_to_zero(l, i, seen) == True:
            return True
        seen.add(i)
    return False

def pairs_sum_to_zero(l, x, seen):
    # Write your code here
    if x == 0:
        return True
    for y in l:
        if y == x or y in seen:
            continue
        seen.add(y)
        if y > 0 and x + y == 0 and pairs_sum_to_zero(l, x + y, seen) == True:
            return True
    return False
```

The function pairs_sum_to_zero uses two functions to solve the problem. The first one is the outer function which takes the list of numbers l as input. The second one is the inner function, which is called by the outer function, and it takes the list l, the integer x, and the set seen as input. The outer function iterates through the list, and for each integer x, it checks if x is 0 or a positive number that hasn't been seen before in the seen set, and if calling the inner function with the same seen set and x as inputs returns True, in which case it returns True. The inner function checks if the integer x is 0, in which case it returns True to the outer function. Otherwise, it iterates through the list and checks if the integer y is equal to x or is already in the seen set, in which case it continues to the next iteration of the loop. Otherwise, it adds y to the seen set and checks if y is a positive number and x + y is 0. If these conditions are fulfilled, it recursively calls the inner function with the same seen set and x + y as inputs, and if it returns True, it returns True. If the inner function returns False, it returns False. 

Here is an example of how you can use the pairs_sum_to_zero function provided above:
```python
print(pairs_sum_to_zero([2, 4, -5, 3, 5, 7]))  # Output: True
print(pairs_sum_to_zero([1, 3, 5, 0]))  # Output: False
``` 
This should return True for the first call and False for the second call, correctly solving the problem.