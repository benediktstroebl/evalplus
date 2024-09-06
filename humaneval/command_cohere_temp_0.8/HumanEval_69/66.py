```python
def search(lst):
    freq, max_val = -1, 0 
    for n in lst:
        if n > max_val:
            max_val = n 
        if n >= freq:
            freq = n 
    return max_val if max_val >= freq else -1
```
The `search` function iterates through the list `lst`, tracking the maximum value found so far (`max_val`) and the frequency of the current number in the list (`freq`). If a number greater than the current `max_val` is seen, `max_val` is updated. Moreover, if the current number's frequency is greater than or equal to its value, `freq` is updated. Finally, the function returns the greatest integer whose frequency meets the criterion, or -1 if none is found. 

Here is a snippet of a possible test suite to ensure the function correctness:
```python
def test_search():
    # Basic Example
    assert search([4, 1, 2, 2, 3, 1]) == 2
    assert search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3
    assert search([5, 5, 4, 4, 4]) == -1

    # Edge Cases
    assert search([10, 5, 1, 1, 1, 5, 5, 5, 10]) == 10
    assert search([1]) == -1
    assert search([]) == -1

    # Large List
    assert search([1] * 1000 + [2] * 1000) == 2

    # Multiple Occurrences of Maximum Frequency
    assert search([1, 2, 2, 3, 1, 1, 3, 2, 2]) == 2
``` 
The test suite covers various scenarios, including edge cases, to ensure the function performs as expected.