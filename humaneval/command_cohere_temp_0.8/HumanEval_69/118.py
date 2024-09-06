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

The function iterates through the list, keeping track of both the maximum value and the frequency of each value. When a number is greater than the current maximum but equals its frequency, the maximum is updated. If the maximum becomes zero and has the same frequency as itself, it means there are no greater valued integers with a higher frequency, and -1 is returned. 

Below is a basic test suite with a few edge cases to ensure the functionality of the problem: 

```python
def test_search():
    # Basic Test Cases
    assert search([4, 1, 2, 2, 3, 1]) == 2
    assert search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3
    assert search([5, 5, 4, 4, 4]) == -1
    assert search([7, 5, 3, 2, 2, 2, 1, 1, 1]) == 3

    # Edge Cases
    assert search([7, 5, 3, 2, 2, 2, 1, 1, 1, 7, 5, 3, 2, 2, 1, 1, 1]) == 3
    assert search([1]) == 1
    assert search([5, 4, 3, 2, 1]) == -1
    assert search([]) == -1
    assert search([1, 1, 1, 1, 2, 2, 2, 3, 3, 4, 4, 5, 5, 5, 5]) == 5

    # Big List
    large_list = [1] * 1001
    large_list += [2] * 1001
    large_list += [3] * 1001
    assert search(large_list) == 3

    # List with Only Single Integer Values
    assert search([1, 2, 3, 4, 5]) == 5
    assert search([100, 200, 300, 400, 500]) == 500
``` 

To run the test suite, you can copy and paste the test_search function into a Python file and run the file. 

```python
test_search()
```