```python
def search(lst):
    freq, max_val = dict(), 0
    for n in lst:
        if n > 0:
            freq[n] = freq.get(n, 0) + 1
            max_val = max(max_val, freq[n])
    return -1 if max_val < 1 else max(n for n in freq if freq[n] >= n)
```
The `search` function takes a list of integers `lst` as input and returns the greatest integer that meets the criteria described in the problem statement. Here is an explanation of the logic:
It initializes a dictionary `freq` to store the frequency of each integer in the list and a variable `max_val` to store the maximum frequency value.

Then it iterates through each integer in the list, and for each positive integer `n`, it updates its frequency in the `freq` dictionary. Simultaneously, it compares the current maximum frequency value with the frequency of `n`, updating `max_val` if the current frequency is greater. 

Finally, the function returns -1 if the maximum frequency value (`max_val`) is less than 1, indicating that no integer in the list meets the specified criteria. If `max_val` is greater than or equal to 1, it returns the greatest integer `n` from the `freq` dictionary whose frequency is greater than or equal to `n`, using a max lookup.

This solution works efficiently in `O(n)` time complexity, where `n` is the length of the input list.