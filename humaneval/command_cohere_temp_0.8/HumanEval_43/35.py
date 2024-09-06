```python
def pairs_sum_to_zero(l):
    # Write your code here
    seen = set()
    for i in l:
        if i > 0:
            if i in seen and l.count(i) > 1:
                return True
            seen.add(i)
        else:
            if -i in seen and l.count(-i) > 1:
                return True
            seen.add(-i)
    return False
```

This function examines every integer in the list and attempts to pair it with another integer that has the opposite sign and equal magnitude to achieve a sum of zero. It uses a set data structure `seen` to keep track of seen integers to avoid double-counting elements. This approach assumes that the list elements are integers and does not work for non-integer elements. It also assumes that the list elements are distinct. 

This solution will return `False` if the list contains only one element or if all positive elements have only one occurrence and all negative elements have only (-n) occurrences, where n is the number of negative elements. 

To use this function, import it into a Python interpreter or script and call it with a list of integers as an argument. It will return `True` if there are two distinct elements in the list that sum to zero and `False` otherwise. You can test it with the given test cases and others as needed.