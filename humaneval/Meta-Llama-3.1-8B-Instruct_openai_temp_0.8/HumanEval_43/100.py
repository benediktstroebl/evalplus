### pairs_sum_to_zero Function
#### Python Script

```python
def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that 
    sum to zero, and False otherwise.
    
    Parameters:
    l (list): A list of integers.
    
    Returns:
    bool: True if there are two distinct elements that sum to zero, False otherwise.
    """
    seen = set()
    for num in l:
        if -num in seen:
            return True
        seen.add(num)
    return False

# Example usage:
print(pairs_sum_to_zero([1, 3, 5, 0]))  # False
print(pairs_sum_to_zero([1, 3, -2, 1]))  # False
print(pairs_sum_to_zero([1, 2, 3, 7]))  # False
print(pairs_sum_to_zero([2, 4, -5, 3, 5, 7]))  # True
print(pairs_sum_to_zero([1]))  # False
```

In this script, we define the function `pairs_sum_to_zero(l)`. This function takes a list `l` of integers as input and checks if there are two distinct elements in the list that sum to zero.

We use a set `seen` to keep track of the numbers we have seen so far. For each number `num` in the list, we check if `-num` is in the set. If it is, it means we have found two numbers that sum to zero, so we return `True`.

If we finish checking all numbers in the list without finding a pair that sums to zero, we return `False`. The time complexity of this solution is O(n), where n is the length of the input list.