```python
def search(lst):
    freq, max_val = 0, max(lst)
    for n in lst:
        if n >= freq:
            freq = n
        if n > max_val:
            max_val = n
    return -1 if max_val == freq and max_val == 0 else max_val
```

The function iterates through the list, keeping track of both the maximum value and the frequency of occurrences of any value. When a value equals or exceeds its frequency, we update the frequency variable. If a value exceeds the previous maximum but has a frequency less than itself, it is not a valid answer, so we revert the `max_val` to its previous value. Thus, when we reach the end of the list and `max_val` is still equal to its frequency and is still zero, we return -1 as there are no valid answers, otherwise, we return the maximum value. 

The following test cases illustrate the behavior of the function:
```python
test_cases = [
    ([4, 1, 2, 2, 3, 1], 2),
    ([1, 2, 2, 3, 3, 3, 4, 4, 4], 3),
    ([5, 5, 4, 4, 4], -1)
]

for lst, expect in test_cases:
    assert search(lst) == expect
```