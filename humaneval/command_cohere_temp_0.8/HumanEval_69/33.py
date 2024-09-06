```python
def search(lst):
    freq, max_val = dict(), 0
    for n in lst:
        if n <= 0:
            continue
        freq[n] = freq.get(n, 0) + 1
        max_val = max(max_val, freq[n])
    return -1 if max_val < 1 else max(n for n in freq if freq[n] >= n)
```
The `search` function iterates through the list, maintaining a dictionary of frequency counts and finding the maximum value with a frequency equal to or greater than itself. This value is then returned, and the function returns -1 if no such value is found. 

Here is an example usage for the function for the input list `[4, 1, 2, 2, 3, 1]`:
```python
search([4, 1, 2, 2, 3, 1])
```
Which would output:
```bash
2
``` 

The greatest integer that is greater than zero and meets the frequency requirement is 2, as it appears twice in the list. 

Let me know if you would like to proceed to another problem or if you have any further questions!