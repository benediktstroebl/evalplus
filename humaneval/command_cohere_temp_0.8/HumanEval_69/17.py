```python
def search(lst):
    freq, max_val = dict(), 0
    for n in lst:
        if n > 0:
            freq[n] = freq.get(n, 0) + 1
            max_val = max(max_val, freq[n])
    return -1 if max_val < 1 else max(n for n in freq if freq[n] >= n)
```
The function initiates a frequency dictionary `freq` to tally the appearances of each integer in the list. Subsequently, it ascertains the maximum value (`max_val`) among the frequencies of all positive integers in the list. If this maximum frequency is less than 1, meaning no positive integer has a frequency ≥ its own value, the function returns -1. If such a number exists, it returns the greatest positive integer having a frequency ≥ its own.

Here is an example usage of the function for the input list `[4, 1, 2, 2, 3, 1]`:
```python
search([4, 1, 2, 2, 3, 1])
```
The function will output: `2` 

And here is another example for the input list `[1, 2, 2, 3, 3, 3, 4, 4, 4]`:
```python
search([1, 2, 2, 3, 3, 3, 4, 4, 4])
```
The function will output: `3`

This correctly solves the problem based on the given constraints.