```python
def search(lst):
    freq, max_val = -1, 0
    for n in lst:
        if n > 0:
            freq = lst.count(n)
            if freq >= n:
                if n > max_val: max_val = n
    return -1 if max_val == 0 else max_val
```

The function `search` iterates through the list `lst`, tracking the frequency of each integer. When it finds an integer greater than zero, it compares its frequency against itself; if the frequency is greater than or equal to the value of the integer, the function updates the `max_val` to this integer's value. Ultimately, the function returns -1 if `max_val` remains 0 (indicating no eligible integer is found), and the maximum eligible value otherwise. 

The following test cases illustrate the behavior of the function:
```python
> search([4, 1, 2, 2, 3, 1])
2
> search([1, 2, 2, 3, 3, 3, 4, 4, 4])
3
> search([5, 5, 4, 4, 4])
-1
```

This suite of tests helps validate the function's behavior against the original problem statement.