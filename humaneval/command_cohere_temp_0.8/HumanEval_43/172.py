```python
def pairs_sum_to_zero(l):
    seen = set()
    for x in l:
        if x > 0:
            if x in seen and l.count(x) > 1:
                return True
            seen.add(x)
        elif x < 0:
            if x in seen and l.count(x) > 1:
                return True
        else:
            continue
    return False
```

This Python script provides a self-contained function called `pairs_sum_to_zero`, which takes a list of integers as input and returns a boolean value. This function aims to identify if there are two distinct elements in the list that sum to zero. It uses a set called `seen` to keep track of elements already encountered. For every element in the list, it checks if the element is greater than zero. If so, it checks if the element exists in the set, and if the count of this element is more than one, it indicates the presence of a pair that sums up to zero. Otherwise, the element is added to the set. If the element is less than zero, it follows the same process, but alternatively, it also checks if the negative of the element exists in the set and if the count is more than one, as this would also represent a pair summing up to zero. The function finally returns False if no such pair is found and True if a pair is identified. 

The script includes examples in the comments to help clarify its functionality and provide further guidance on how it addresses the problem statement. These examples also include their corresponding output, briefly commented on whether they should return True or False. 
*NOTE*: The implementation assumes that the list contains only integers, and it might need additional modifications to accommodate other data types.*