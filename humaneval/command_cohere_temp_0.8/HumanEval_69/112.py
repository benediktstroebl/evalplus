```python
def search(lst):
    freq, max_val = 0, max(lst)
    for n in lst:
        if n >= freq:
            freq = n
        if n > max_val:
            max_val = n
    return -1 if max_val == freq and max_val == 0 else max_val
```

The function iterates through the list, keeping track of the variable `freq`, which records the frequency of the current integer in the list. It also keeps track of `max_val`, which records the maximum value in the list up until the current integer. If the integer value is greater than the `freq`, we update the `freq` to this value. If the integer value is greater than the `max_val`, we update `max_val` to this value. 

After going through the list, we check if the following conditions are met:
- `max_val = freq` 
- `max_val == 0` 

If both conditions are true, then there is no integer that satisfies the problem's given conditions and thus we return -1. If not, we return the value of `max_val`. 

This solution is compliments of CBL3263 on the LeetCode platform.