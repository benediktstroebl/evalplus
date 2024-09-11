### pairs_sum_to_zero Function

Below is a Python script that defines the `pairs_sum_to_zero` function. This function checks if there are two distinct elements in the list that sum to zero.

```markdown
### Code
```python
def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    """
    # Create a set to store the elements we have seen so far
    seen = set()
    
    # Iterate over the list
    for num in l:
        # Check if -num is in the set (i.e., we have seen its negative)
        if -num in seen:
            # If we have seen the negative of this number, return True
            return True
        # Add this number to the set
        seen.add(num)
    
    # If we have iterated over the entire list and haven't found a pair that sums to zero, return False
    return False
```

### Example Use Cases
```markdown
# Test the pairs_sum_to_zero function
print(pairs_sum_to_zero([1, 3, 5, 0]))  # False
print(pairs_sum_to_zero([1, 3, -2, 1]))  # False
print(pairs_sum_to_zero([1, 2, 3, 7]))  # False
print(pairs_sum_to_zero([2, 4, -5, 3, 5, 7]))  # True
print(pairs_sum_to_zero([1]))  # False
```

### Explanation
This function works by iterating over the list and checking if the negative of each number is in a set of numbers it has seen so far. If it has seen the negative of a number, it means that there are two numbers in the list that sum to zero, so it returns True. If it iterates over the entire list without finding such a pair, it returns False. The set is used to keep track of the numbers it has seen so far, which allows it to check if a number's negative has been seen in constant time.