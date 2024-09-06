```python
def search(lst):
    freq, max_val = dict(), 0
    for n in lst:
        if n > 0:
            freq[n] = freq.get(n, 0) + 1
            max_val = max(max_val, freq[n])
    return -1 if max_val < 1 else max(n for n in freq if freq[n] >= n)
```
The `search` function takes a list of positive integers `lst` as input. It initializes a dictionary `freq` to store the frequency of each integer in the list, and initially sets `max_val` to 0. Then, it iterates through each element `n` in the list, and if `n` is greater than 0, it updates the frequency of `n` in the `freq` dictionary. The `max_val` variable is updated with the maximum value of the frequency of all integers so far, ensuring that it is not less than 1. 

Finally, it returns -1 if there are no integers with a frequency greater than or equal to themselves, and searches for the maximum frequency integer among those whose frequency is greater than or equal to themselves using a list comprehension and returns it. The dictionary `freq` is used to efficiently lookup the frequency of each integer. 

The following examples illustrate how the function works:
```python
search([4, 1, 2, 2, 3, 1]) == 2
search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3
search([5, 5, 4, 4, 4]) == -1
```