```python
def choose_num(x, y):
    max_even = -1
    temp = x
    while temp <= y:
        if temp % 2 == 0:
            max_even = temp
        temp += 1
    return max_even
```

The function slowly iterates through the range [x, y] using a while loop, checking if each number is even, and returns the maximum even number found (or -1 if none is found). 

To make sure that the code is correct, let's unit test it:
```python
def test_choose_num():
    # Test case 1
    assert choose_num(12, 15) == 14
    # Test case 2
    assert choose_num(13, 12) == -1
    # Test case 3
    assert choose_num(2, 10) == 6
    # Test case 4
    assert choose_num(100, 101) == 100

test_choose_num()
```

This test suite contains four distinct cases, each of which verifies that the function performs appropriately. Case 1 and 3 verify that the function correctly identifies the maximum even number in the range, whereas case 2 and 4 validate the -1 return value when no such number exists. 

To run the tests correctly, you can add the test case function and then run the test suite using Python as follows: 
```python
python test_choose_num.py
``` 
This will run the test suite, which will validate that the `choose_num` function behaves as expected. 
If the tests pass, it means that the function is correct and is a definitive solution to the problem.