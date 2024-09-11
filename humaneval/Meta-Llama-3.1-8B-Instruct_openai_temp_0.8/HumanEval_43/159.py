### pairs_sum_to_zero Function
```python
def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that sum to zero, and False otherwise.
    
    Parameters:
    l (list): A list of integers.
    
    Returns:
    bool: True if there are two distinct elements that sum to zero, False otherwise.
    """
    seen = set()  # Initialize an empty set to store the elements we have seen so far
    for num in l:  # Iterate over the list
        complement = -num  # The complement of num is the number that, when added to num, gives 0
        if complement in seen:  # If we have seen the complement before
            return True  # Then there are two distinct elements that sum to zero, so return True
        seen.add(num)  # Add num to the set of seen elements
    return False  # If we have iterated over the whole list and haven't found any pair of elements that sum to zero, return False

# Test cases
print(pairs_sum_to_zero([1, 3, 5, 0]))  # False
print(pairs_sum_to_zero([1, 3, -2, 1]))  # False
print(pairs_sum_to_zero([1, 2, 3, 7]))  # False
print(pairs_sum_to_zero([2, 4, -5, 3, 5, 7]))  # True
print(pairs_sum_to_zero([1]))  # False
```
This script uses a set to keep track of the elements we have seen so far. It checks if the complement of each element (i.e., the number that, when added to the current element, gives 0) is in the set of seen elements. If it is, it means we have found a pair of elements that sum to zero, so we return True. If we have iterated over the whole list and haven't found any such pair, we return False.