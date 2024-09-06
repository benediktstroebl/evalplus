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

The function first creates a dictionary `freq` whose keys are the elements of `lst` and the values are their frequencies, that is the number of times each element appears in the list. Then it iterates over the keys of the `freq` dictionary and maximizes the variable `max_val` with the frequencies of each integer, then iterates over the keys of the `freq` dictionary again to find if there is any integer whose frequency is greater than or equal to its own value, and returns it if it exists, or returns `-1` if there is no such integer. 

Here is a test suit to validate the functionality of the search function:
```python
def test_search():
    assert search([4, 1, 2, 2, 3, 1]) == 2
    assert search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3
    assert search([5, 5, 4, 4, 4]) == -1
    assert search([1, 2, 3, 4, 5]) == -1
    assert search([1, 2, 3, 4, 5, 6, 7, 8, 9]) == -1
```

The test suite can be executed using the `pytest` framework, which needs to be installed separately with the following command: 
```bash
pip install pytest
``` 

The tests can then be executed in Python like this: 
```bash
python -m pytest
``` 

The execution of the previous command will run the test suite and display the results, if all test passes, the output should be something like this:
```plaintext
test_search ... ok
```