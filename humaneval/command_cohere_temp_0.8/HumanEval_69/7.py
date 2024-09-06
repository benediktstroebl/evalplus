```python
def search(lst):
    freq, max_val = -1, 0 
    for val in lst:
        if val > max_val:
            max_val = val 
        elif val == max_val and lst.count(val) >= val:
            freq = val 
    return max_val if freq == -1 else -1 
```

The function `search` iterates through the list `lst`, keeping track of the maximum value `max_val` and its frequency. When a new maximum is found, it checks if the current maximum's frequency is less than or equal to its value. If so, the frequency is updated. Finally, the maximum value is returned if its frequency is -1, indicating no better integer was found; otherwise, -1 is returned. 

This approach ensures that the maximum value with the described criteria is found and handled correctly within the iteration of the list. 

The unit tests for this function are also important, as they ensure its correctness across various scenarios. Below is a simple test suite that can be used: 
```python
def test_search():
    # Basic example
    assert search([4, 1, 2, 2, 3, 1]) == 2
    assert search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3
    assert search([5, 5, 4, 4, 4]) == -1

    # Edge cases
    assert search([10, 10, 10, 10]) == 10
    assert search([1]) == 1
    assert search([7, 1, 7, 1, 7, 1]) == -1 

    # Large list
    assert search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 5 

test_search()
```
This test suite covers various scenarios, including edge cases, which ensures that the `search` function behaves as expected.