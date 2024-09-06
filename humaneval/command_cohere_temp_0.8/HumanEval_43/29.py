```python
def pairs_sum_to_zero(l):
    seen = set()
    for x in l:
        if x > 0:
            if x in seen and l.count(x) > 1:
                return True
            seen.add(x)
        else:
            if (-x) in seen and l.count(-x) > 1:
                return True
            seen.add(-x)
    return False
```

This function iterates through the list, tracking integers it has seen.

For positive integers, it checks if the integer has been seen before and whether there are more than one such integer in the list.

For negative integers, it checks if the negation of the integer has been seen before and whether there are more than one such integers in the list.

It returns `True` if any such pair is found, and `False` otherwise.

The function is encapsulated in a self-contained code block ready for inclusion in a larger codebase and utilizes built-in Python sets and iterators to efficiently solve the problem. It also adheres to the problem statement's expected behavior as stated in the provided markdown code block.