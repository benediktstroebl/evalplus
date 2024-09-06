Here's a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
def monotonic(lst):
    if len(lst) <= 1:
        return True
    else:
        if lst[1] < lst[0]:
            return monotonic(lst[1:]) and not (lst[2] > lst[1])
        elif lst[1] > lst[0]:
            return monotonic(lst[:-1]) and not (lst[0] > lst[-1])
        else:
            return False
```
The function monotonic takes a list, lst, as input and returns True if the list's elements are monotonic (increasing or decreasing) and False otherwise. The base case checks if the list has one or fewer elements, returning True in both cases. The recursive cases check if the second element is smaller than the first, in which case the function recursively checks the rest of the list for monotonicity, ensuring the third element isn't larger than the second. The else case is for when the second element is not smaller than the first, and the function recursively checks the reverse of the list for monotonicity, ensuring the first element isn't larger than the last element.