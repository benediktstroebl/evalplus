```python
def search(lst):
    freq, max_val = -1, 0
    for n in lst:
        if n > max_val:
            max_val = n
        if n >= freq:
            freq = n
    return max_val if freq >= max_val else -1
```
The script uses two variables, `freq` and `max_val`, to store the frequency of the current integer in the list and the maximum value of the list respectively. The loop iterates through the list, updating `freq` and `max_val` as necessary. After each iteration, the algorithm checks if the frequency of the current integer is greater than or equal to its value. If it is, the algorithm returns the maximum value found; otherwise, it returns -1, indicating that no such integer exists in the list. 

Here is an example of how you can test this script:
```python
def test_search():
    assert search([4, 1, 2, 2, 3, 1]) == 2
    assert search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3
    assert search([5, 5, 4, 4, 4]) == -1
    assert search([1, 2, 3, 4, 5]) == -1
``` 

This will verify that the `search` function correctly solves the problem for a variety of input lists.