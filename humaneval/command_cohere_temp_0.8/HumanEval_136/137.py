```python
def largest_smallest_integers(lst):
    positive = min(lst, key=lambda x: x >= 0)
    negative = max(lst, key=lambda x: x < 0)
    return negative, positive
```

The function `largest_smallest_integers` uses the `min` and `max` functions with a custom key to find the smallest positive and largest negative integers in the list. The key is a lambda function that returns `True` if the integer is negative, and `False` if it's positive, which helps to identify the largest negative and smallest positive numbers in the list.

Here is a test suite to ensure it works:
```python
def test_largest_smallest_integers():
    assert largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (1, 1)
    assert largest_smallest_integers([0]) == (None, None)
    assert largest_smallest_integers([-3, -1, -7, -11, -15]) == (-3, -15)
    assert largest_smallest_integers([]) == (None, None)
``` 

To run the test suite, you can copy and paste the test cases into a Python interpreter or save them in a `.py` file and run using the command line:
```bash
python test_largest_smallest_integers.py
``` 
Alternatively, you can use an IDE or testing framework to automate and organize your tests more efficiently.