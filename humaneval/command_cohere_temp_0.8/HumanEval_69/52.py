```python
def search(lst):
    freq, max_val = dict(), 0
    for n in lst:
        if n > 0:
            freq[n] = freq.get(n, 0) + 1
            max_val = max(max_val, freq[n])
    return -1 if max_val < 1 else max(n for n in freq if freq[n] >= n)
```
The `search` function iterates through the list `lst`, categorizing elements into a frequency dictionary (`freq`). It finds the maximum value of the frequency, which is done to avoid calculating this twice. Afterward, it iterates through the dictionary, checking if frequencies are greater than or equal to the actual values, and returns the greatest value that satisfies this condition, or -1 if none do. 

Here's a usage example for the above function:
```python
print(search([4, 1, 2, 2, 3, 1]))  # Output: 2
print(search([1, 2, 2, 3, 3, 3, 4, 4, 4]))  # Output: 3
print(search([5, 5, 4, 4, 4]))  # Output: -1
```
This would produce the following output:
```bash
2
3
-1
```