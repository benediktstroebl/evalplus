```python
def will_it_fly(q, w):
    return (len(q) == 1 or q == q[::-1]) and sum(q) <= w
```

The function `will_it_fly` uses two conditions to determine if an object will fly:
1. The length of the query list `q` is equal to 1 or it is a palindrome. A palindrome is a sequence that reads the same forwards and backwards, `q == q[::-1]`. 
2. The sum of the elements in the list `q` is less than or equal to the maximum weight `w`. 

These conditions ensure that the object is balanced and light enough to fly.

This code includes tests to ensure correct functionality:
```python
def test_will_it_fly():
    # True: Single element is always balanced and sum of elements is less than weight
    assert will_it_fly([3], 5) == True
    assert will_it_fly([8], 8) == True

    # False: Palindrome but sum of elements exceeds weight
    assert will_it_fly([1, 2], 5) == False
    assert will_it_fly([3, 2, 3], 1) == False

    # True: Palindrome and sum of elements less than weight
    assert will_it_fly([3, 2, 3], 9) == True
    assert will_it_fly([1, 2, 3, 2, 1], 10) == True

    # False: Not a palindrome but sum of elements is less than weight
    assert will_it_fly([1, 2, 3], 5) == False
    assert will_it_fly([4, 3, 2, 1], 5) == False

test_will_it_fly()
```

You can copy and paste this code into a Python environment or script to test out the functionality. Feel free to modify the code and tests to suit your needs.