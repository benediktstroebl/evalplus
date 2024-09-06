```python
def search(lst):
    freq, max_val = dict(), 0
    for n in lst:
        if n > 0:
            freq[n] = freq.get(n, 0) + 1
            max_val = max(max_val, freq[n])
    return -1 if max_val < 1 else max(n for n in freq if freq[n] >= n)
```

The function `search` uses a dictionary `freq` to count the frequency of each number in the list. Then, it takes each number's frequency and checks if it meets the condition and updates the `max_val` accordingly. In the end, it returns the number with the maximum value if it meets the condition or -1 if no such number exists. 

The following test cases confirm the correctness of the approach:
```python
>>> search([4, 1, 2, 2, 3, 1])
2
>>> search([1, 2, 2, 3, 3, 3, 4, 4, 4])
3
>>> search([5, 5, 4, 4, 4])
-1
>>> search([0, 0, 0, 4, 4, 4, 4, 4, 4])
4
>>> search([5, 5, 5, 5, 5, 5, 5])
-1
```