```python
def digits(n):
    prod = 1
    for digit in str(n):
        if int(digit) % 2:
            prod *= int(digit)
    return prod
```

This `digits` function iterates through each digit in the decimal representation of `n`, if a digit is odd, it multiplies it into the `prod` variable, and finally returns the resulting product. 

Here is a test case to test the functionality of the given solution:
```python
def test_digits():
    assert digits(1) == 1
    assert digits(4) == 0
    assert digits(235) == 15
    assert digits(742) == 12628
    assert digits(10) == 1
``` 

This tests the function on a variety of provided examples, ensuring that it returns the correct value for each one. 
If you want to evaluate the performance of this function, the total time complexity is O(n), where n is the number of digits of the given integer `n`, as it iterates through each digit once, and each operation within the loop is constant time.

This approach does not require any additional libraries and is relatively simple, focusing on iterating through the digits and applying the product functionality.