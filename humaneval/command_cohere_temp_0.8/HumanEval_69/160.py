```python
def search(lst):
    freq, max_val = dict(), 0
    for n in lst:
        if n > 0:
            freq[n] = freq.get(n, 0) + 1
            max_val = max(max_val, freq[n])
    return -1 if max_val < 1 else max(n for n in freq if freq[n] >= n)
```
The function iterates through the list and uses a dictionary to track the frequency of each integer. Then the greatest integer that satisfies the condition is returned, with -1 if no such integer exists. 

The script includes corresponding unit tests:
```python
def test_search():
    assert search([4, 1, 2, 2, 3, 1]) == 2
    assert search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3
    assert search([5, 5, 4, 4, 4]) == -1
    assert search([6, 6, 6, 7, 5, 5, 5, 4, 4, 4]) == 6
    assert search([7, 8, 8, 9, 9, 10, 10, 11, 12, 12]) == 9
    assert search([13, 14, 15, 16, 17, 17, 18, 19, 20, 20]) == 20
    assert search([21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == -1
``` 

You can use a Markdown code block to include this code alongside the test code for reproduction:
```python
def test_search():
    assert search([4, 1, 2, 2, 3, 1]) == 2
    assert search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3
    assert search([5, 5, 4, 4, 4]) == -1
    assert search([6, 6, 6, 7, 5, 5, 5, 4, 4, 4]) == 6
    assert search([7, 8, 8, 9, 9, 10, 10, 11, 12, 12]) == 9
    assert search([13, 14, 15, 16, 17, 17, 18, 19, 20, 20]) == 20
    assert search([21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == -1
``` 
This allows you to run the test and verify the function's correctness.