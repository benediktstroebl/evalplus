```python
def search(lst):
    freq, max_val = dict(), 0
    for n in lst:
        if n > 0:
            freq[n] = freq.get(n, 0) + 1
            max_val = max(max_val, freq[n])
    return -1 if max_val < 1 else max(n for n in freq if freq[n] >= n)
```
The `search` function takes a list of integers `lst` as input. It initializes a dictionary `freq` to store the frequency of each integer, and initially assumes the maximum value among the integers to be 0 (`max_val`).

Then, for each element `n` in the list:
- If `n` is greater than 0, it updates the frequency of `n` in the `freq` dictionary.
- It also updates `max_val` with the maximum value between its current value and the frequency of `n`.

Finally, the function returns -1 if `max_val` is less than 1 (meaning there are no positive integers with a frequency greater than or equal to itself). Otherwise, it returns the greatest positive integer that satisfies the condition.

The logic of the function assumes that the list contains only positive integers, and that there are no duplicate elements in the list.