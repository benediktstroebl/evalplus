```python
def pairs_sum_to_zero(l):
    # Write your code here
    seen = set()
    for i in l:
        if i > 0:
            twice_i = 2 * i
            if twice_i in seen:
                return True
            seen.add(i)
        else:
            neg_i = -i
            if neg_i in seen:
                return True
            seen.add(i)
    return False
```

This function takes a list of integers and returns `True` if there are two distinct elements in the list that sum to zero and `False` otherwise. It does this by checking if there is a pair of the form `(i, -i)` where `i` is a positive integer and not encountering duplicates. This is done using a set to keep track of seen elements. It returns `True` if such a pair exists and `False` otherwise. It is important to note that the function carefully avoids duplication in the seen set using the positive value as well as the negative `-i` value.  Overall, the code's efficiency is dictated by the set's performance, which typically has a time complexity of O(1) for operations like `add` and `contains`.