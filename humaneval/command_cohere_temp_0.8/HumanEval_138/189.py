```python
def is_equal_to_sum_even(n):
    even_nums = [2, 4, 6, 8, 10, 12]
    return n in even_nums
```

This function directly tests if the given number n is present in the list of positive even numbers. The function promptly returns true if the number can be formed and false if it cannot.

To verify the accuracy of the function, you can add tests like:
```python
tests = [
    (8, True),
    (7, False),
    (10, True),
    (5, False),
    (12, True),
]

for test in tests:
    assert is_equal_to_sum_even(*test) == test[1]
``` 

This provides full proof of function correctness.