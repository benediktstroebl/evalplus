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
The code utilizes a dictionary (`freq`) to maintain the frequency of each number on the list. After iterating through the list, the script calculates the maximum value of an integer with its frequency being greater than or equal to its value. To ensure a correct result, the script checks if the maximum frequency is less than 1, returning -1 if so, to indicate that no valid answer exists. Lastly, the output is the maximum value within the aforementioned criteria after sorting the frequencies.

Here is a test suite to ensure the function behaves correctly:
```python
def test_search():
    assert search([4, 1, 2, 2, 3, 1]) == 2
    assert search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3
    assert search([5, 5, 4, 4, 4]) == -1
    assert search([10, 10, 10, 5, 4, 4]) == 10
    assert search([1, 2, 3, 4, 5, 5, 6, 6, 7, 8, 9, 10, 10, 10]) == 10
    assert search([12, 12, 11, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 12
    assert search([13, 13, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 13
``` 
The test suite contains a diverse set of inputs to validate the function's behavior in different scenarios.