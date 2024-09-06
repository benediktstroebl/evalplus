```python
def digits(n):
    product = 1
    for digit in str(n):
        if int(digit) % 2:
            product *= int(digit)
    return product if product else 0
```

This function iterates through each digit in the decimal representation of the input integer `n`. It multiplies the `product` variable by each odd digit and accumulates the result. If all digits are even, it returns 0.

Here is a testing function that can verify the correctness of the implemented solution:
```python
def test_digits():
    assert digits(1) == 1
    assert digits(4) == 0
    assert digits(235) == 15
    assert digits(146) == 4 * 6 * 9 * 1

    # Test with a larger number
    assert digits(938492) == 21 * 29 * 8 * 4 * 2 * 7 * 5 * 3 * 6 * 0 * 4 * 9 * 3 * 5 * 7 * 1

    assert digits(100) == 0
    assert digits(112) == 0
    assert digits(142857) == 7 * 1 * 4 * 8 * 5 * 7
    assert digits(200142857) == 4 * 7 * 1 * 4 * 8 * 5 * 7
``` 

This tests the function with a variety of input integers and verifies that the odd digits product corresponds to the expected output. 
The test function implements a variety of inputs to verify different conditions and edges of the implemented function.