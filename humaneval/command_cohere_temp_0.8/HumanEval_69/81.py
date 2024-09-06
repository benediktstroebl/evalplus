```python
def search(lst):
    freq, max_val = -1, 0
    for n in lst:
        if n > 0:
            freq = lst.count(n)
            if freq >= n and (max_val < 0 or n > max_val):
                max_val = n
    return max_val if max_val > 0 else -1
```

The function `search` takes a list of integers `lst` as input and returns the greatest integer that meets the conditions stated in the problem prompt. It first creates a variable `freq` to track the frequency of the current integer in the list and a `max_val` to keep track of the largest valued integer it has encountered so far that meets the conditions. Then, it iterates through the list. If the current integer is greater than zero, it checks if the frequency of the integer is greater than or equal to its value and whether it is larger than the current `max_val`. If it is, it updates `max_val` and `freq` accordingly. After checking all integers in the list, it returns `max_val` if it is greater than zero, and `-1` otherwise.

The code assumes that the list contains only positive integers and that the list is non-empty. These assumptions are present in the problem statement, and a clarification should be made if they are not true in the context where the code will be used. 

This solution is efficient because it uses linear iteration and has a time complexity of O(n), where n is the number of elements in the input list `lst`. It is possible to optimize this to a logarithmic solution using a binary search approach, but that is a more complex implementation. 

Note that the code assumes that the list elements are integers. If the list elements are of an alternative data type, such as strings, the code can still run but may not produce the intended results. If this is the case, a content-aware update would be needed.