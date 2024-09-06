```python
def exchange(lst1, lst2):
    res = 'NO'
    # Check if any element of lst1 is odd
    if any(x % 2 for x in lst1):
        # Exchange odd elements with lst2
        lst1, lst2 = lst2, lst1
        res = 'YES'
    return res
```

The approach used in the code can be described as follows:
1. At first, we assume that the function returns 'NO' because there is no exchange that can be done.
2. We check if any element of `lst1` is odd using the `any()` function and a generator expression that calculates the modulo of each element by 2.
3. If all elements of `lst1` are even, we don't need to do anything and the answer is 'YES'. Otherwise, we proceed to the next step.
4. We exchange `lst1` and `lst2` using the tuple unpacking technique because all the odd elements in `lst1` should be exchanged with the even elements in `lst2` to make `lst1` full of even numbers.
5. Finally, we return the answer as 'YES'.