```python
def is_sorted(lst):
    dups = {}
    for n in lst:
        if n in dups:
            dups[n] += 1
        else:
            dups[n] = 1
    return all(dups[n] == 1 for n in dups if dups[n] != 1)
```

The function employs a simple logic to check for duplicates in the list. It uses a dictionary to track the frequency of each number, then checks if all frequencies are strictly 1, except for the case when the list is empty, which is handled by the all() function. The provided example use cases are covered in the unit tests included in the code snippet below:
```python
def test_is_sorted():
    assert is_sorted([5])
    assert is_sorted([1, 2, 3, 4, 5])
    assert not is_sorted([1, 3, 2, 4, 5])
    assert is_sorted([1, 2, 3, 4, 5, 6])
    assert is_sorted([1, 2, 3, 4, 5, 6, 7])
    assert not is_sorted([1, 3, 2, 4, 5, 6, 7])
    assert is_sorted([1, 2, 2, 3, 3, 4])
    assert not is_sorted([1, 2, 2, 2, 3, 4])
``` 

To run the tests, you can copy the test function and paste it into a Python file and run the file. Alternatively, you can use the following command directly in your terminal: 
 ```bash
python -m unittest your_test_file.py
``` 
Replace `your_test_file.py` with the name of the file containing the test function.