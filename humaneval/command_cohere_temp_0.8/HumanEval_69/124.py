```python
def search(lst):
    freq, max_val = dict(), 0
    for n in lst:
        if n > 0:
            freq[n] = freq.get(n, 0) + 1
            max_val = max(max_val, freq[n])
    return -1 if max_val < 1 else max(n for n in freq if freq[n] >= n)
```
The `search` function takes a list of positive integers `lst` as input. It initializes a dictionary `freq` to store the frequency of each integer in the list and a variable `max_val` to keep track of the maximum value encountered during the iteration. The function iterates through each integer in the list, and if it's greater than zero, it updates its frequency in the `freq` dictionary. The `max_val` variable is updated with the maximum value of the frequency compared to the integer itself. 

After processing all integers, the function checks if the maximum frequency is less than one (`max_val < 1`). If true, meaning there are no integers with a frequency greater than or equal to themselves, the function returns -1 to indicate that no such integer is found. Otherwise, it returns the greatest integer that meets the criteria by iterating through the keys of the `freq` dictionary and returning the maximum integer with a frequency greater than or equal to itself.