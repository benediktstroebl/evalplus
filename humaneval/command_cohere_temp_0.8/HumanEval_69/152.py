```python
def search(lst):
    freq, max_val = dict(), 0
    for n in lst:
        if n <= 0:
            continue
        elif n in freq:
            freq[n] += 1
        else:
            freq[n] = 1
        max_val = max(max_val, n)
    return -1 if max_val == 0 else max(k for k, v in freq.items() if k >= v)
```

The function first creates a dictionary `freq` to store the frequency of each integer in the list. It then iterates over the list, updating the frequency of each integer and keeping track of the maximum integer found so far (`max_val`). Finally, the function returns -1 if the maximum integer found is 0 (meaning there are no positive integers in the list), or the maximum integer with a frequency greater than or equal to its value. 

This approach uses a dictionary to efficiently track the frequency of each integer and avoids the need for multiple passes through the input list.