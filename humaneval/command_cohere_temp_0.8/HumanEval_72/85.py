```python
def will_it_fly(q, w):
    return (sum(q) <= w) and (w <= len(q) == len(set(q)))
```

The function will return **True** if the object **q** will fly, and **False** otherwise. 

The object **q** will be considered as palindromic and balanced if the length of the set of its elements is equal to the length of the object. Also, the object will be considered as light enough to fly if the sum of its elements is less than or equal to the maximum possible weight **w**. 

Example tests, that can be executed by copying and pasting into a Python file:
```python
def test_will_it_fly():
    assert will_it_fly([1, 2], 5) == False
    assert will_it_fly([3, 2, 3], 1) == False
    assert will_it_fly([3, 2, 3], 9) == True
    assert will_it_fly([3], 5) == True

    assert will_it_fly([1, 1, 1], 6) == False
    assert will_it_fly([1, 1, 1, 1, 1, 1], 10) == True
    assert will_it_fly([2, 2, 2, 2, 2], 10) == True
    assert will_it_fly([3, 3, 3, 3], 5) == False
```
If you want to check against more test cases, these can be added under the test function, and each test case should be executed by calling ```test_will_it_fly()```.