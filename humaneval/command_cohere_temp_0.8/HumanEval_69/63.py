```python
def search(lst):
    freq, max_val = dict(), 0
    for n in lst:
        if n > 0:
            freq[n] = freq.get(n, 0) + 1
            max_val = max(max_val, freq[n])
    return -1 if max_val < 1 else max(n for n in freq if freq[n] >= n)
```
The function `search` takes a list of integers `lst` as input and returns the greatest integer that is greater than zero and has a frequency greater than or equal to the value of the integer itself. The frequency of an integer is the number of times it appears in the list.

The script uses a dictionary `freq` to store the frequency of each integer in the list. Then, it iterates over the list and updates the frequency of each integer. The maximum value is also updated with the frequency of the current integer.

Finally, the script returns -1 if the maximum frequency is less than 1 (meaning there are no valid integers). Otherwise, it returns the maximum value integer that has a frequency greater than or equal to itself.