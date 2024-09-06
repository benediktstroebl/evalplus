```python
def search(lst):
    freq, max_val = -1, 0
    for n in lst:
        if n > max_val:
            max_val = n
        if n >= freq:
            freq = n
    return max_val if freq >= max_val else -1
```
The `search` function traverses the list `lst`, keeping track of the maximum value encountered as `max_val` and the frequency of any integer as `freq`. When an integer's value is greater than the current `max_val`, `max_val` is updated. If an integer's frequency equals or surpasses its own value, `freq` is updated. The function returns `max_val` if `freq` is at least `max_val`; otherwise, it returns `-1` to indicate the absence of any integer that fits the criteria. 

Here is a simpler version of the code:
 ```python
def search(nums):
    freq = {}
    for n in nums:
        if n in freq:
            freq[n] += 1
        else:
            freq[n] = 1
    for n in freq:
        if freq[n] >= n:
            return n
    return -1
```
This version uses a dictionary to keep track of frequencies of integers in the list. The function iterates over the list and updates the frequency of each integer. Then it iterates over the dictionary and checks if any integer has a frequency greater than or equal to its own value. If found, the function returns the integer, if not, it returns -1.  This version uses a dictionary which is generally faster than a list for these kinds of operations.