Here's a Python script with a self-contained function that solves the problem:
```python
def monotonic(lst):
    if len(lst) <= 1:
        return True
    if lst[1] < lst[0]:
        return monotonic(lst[1:]) and not (lst[2] > lst[1])
    if lst[1] > lst[0]:
        return monotonic(lst[:-1]) and not (lst[0] > lst[-1])
    return False
```

The function monotonic takes a list lst as input and returns True if the list's elements are in a monotonic sequence – increasing or decreasing – and False otherwise. The function's logic first handles the base cases of an empty list or a list with one element, both yielding True. It then checks the relation between the first two elements lst[1] and lst[0] to determine whether the sequence is increasing or decreasing. Depending on this relation, the function recursively calls itself on the rest of the list, excluding the first element, and checks if the second element relative to the sequence's direction is not incorrect. The function terminates with False if the sequence is not monotonic.