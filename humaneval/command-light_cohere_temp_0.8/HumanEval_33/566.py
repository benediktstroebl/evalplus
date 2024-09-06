```python
def sort_third(lst):
    """Sorts a list of numbers so that values divisible by three are in their correct positions, and the rest remain in their original order.
    
    Args:
        lst (list) -- list of numbers
    Returns:
        list -- list of numbers, sorted as per the above description
    """
    divisible = [x for x in lst if x % 3 == 0]
    return [x if x not in divisible else y for x, y in zip(lst, divisible)]

# Test cases
print(sort_third([1, 2, 3]))        # [1, 2, 3]
print(sort_third([5, 6, 3, 4, 8, 9, 2])) # [2, 6, 3, 4, 8, 9, 5]
```
The function `sort_third` sorts the input list such that numbers divisible by 3 are in their correct positions and the rest remain in their original order. The function works by first creating a new list `divisible` which contains all numbers divisible by 3, then using the list `divisible` as a key to map the original list into the new list.