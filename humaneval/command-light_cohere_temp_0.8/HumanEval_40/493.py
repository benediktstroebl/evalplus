```python
def triples_sum_to_zero(lst):
    # Sort the list
    lst.sort()
    [
    
    # Initialize a counter to store the sum of three consecutive elements
    count = 0
    curr_sum = 0
    
    # Iterate through the list
    for i in range(1, len(lst)):
        # If the current element is not the first, make sure the sum of the previous two elements is not too large
        if i > 1:
            curr_sum += lst[i - 1]
        if curr_sum > 1:
            return False
        
        # Update the counter
        count += 1
        
        # If the counter reaches three, the list has three elements sum to zero
        if count == 3:
            return True
    
    return False
```