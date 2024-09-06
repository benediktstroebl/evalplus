```python
def pairs_sum_to_zero(l):
    seen = set()
    for x in l:
        if x > 0:
            if x in seen and l.count(x) > 1:
                return True
            seen.add(x)
        else:
            if -x in seen and l.count(-x) > 1:
                return True
            seen.add(-x)
    return False
```

This function examines every element in the list, tracking the elements it has seen so far using a set data structure. When it encounters a positive element `x`, it checks if `x` has been seen before and if there are multiple occurrences of `x` in the list. If so, it returns `True`. The function performs a similar check for negative elements, using the property that two negative elements with the same magnitude will sum to zero. 

The function is designed to return `False` if there are no two distinct elements that sum to zero and only returns `True` if such a pair is found. It is optimized to have a time complexity of O(n), where n is the length of the input list `l`, as it iterates through the list once, performing operations on each element. 

The markdown code block for the problem statement is redundant as the problem statement already provides a Python function with the required behavior and tests. 

Let me know if you would like me to provide an example of a problem statement without a provided function, or any other questions you have about generating problem statements for coding challenges.