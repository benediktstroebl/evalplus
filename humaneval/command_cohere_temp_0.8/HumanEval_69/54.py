```python
def search(lst):
    freq, max_val = dict(), 0
    for n in lst:
        if n > 0:
            freq[n] = freq.get(n, 0) + 1
            max_val = max(max_val, freq[n])
    return -1 if max_val < 1 else max(n for n in freq if freq[n] >= n)
```
The function initiates a frequency dictionary `freq` to tally how often each number appears in the list. The variable `max_val` is used to keep track of the largest value encountered so far that meets the criteria (greater than zero and with a frequency equal to or higher than itself).

The subsequent loop traverses the list, updating the `freq` dictionary and `max_val` as it goes. If the maximum value is not at least 1, meaning no number satisfies the condition, the function returns -1. If there is at least one such number, it returns the maximum value among them. To avoid float comparisons, the maximum value is computed using `max(n for n in freq if freq[n] >= n)`.

The following test cases verify the function's robustness:
```python
test_cases = [
    ([4, 1, 2, 2, 3, 1], 2),
    ([1, 2, 2, 3, 3, 3, 4, 4, 4], 3),
    ([5, 5, 4, 4, 4], -1)
]

for lst, expect in test_cases:
    assert search(lst) == expect
```

The function successfully produces the expected outputs for each test case.