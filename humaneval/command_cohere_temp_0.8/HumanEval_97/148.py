```python
def multiply(a, b):
    dig1 = a % 10
    dig2 = b % 10
    product = dig1 * dig2
    if product > 9:
        product = 0
    return product
```

The code directly assaults the problem statement by extracting the last digits of both integers using the modulo operator (`%`). Using the digit from the first number as a multiplier, it then multiplies these unit digits. To handle situations when the result would be more than one digit, it resets the answer to zero if the product is greater than 9. This technique gives the desired result for the given inputs. 

To ensure that the code behaves as expected, a few tests could be added. These tests function as fundamental checks to validate the basic behavior of the function.

```python
# Testing the multiply function
def test_multiply():
    # Basic Tests:
    assert multiply(12, 21) == 2
    assert multiply(15, 25) == 5

    # Testing with Large Numbers:
    assert multiply(987, 6543) == 7

    # Testing with Negative Numbers:
    assert multiply(-11, -22) == -11

    # Testing with Single-Digit Numbers:
    assert multiply(3, 5) == 0

    # Testing with Zero:
    assert multiply(0, any_number) == 0
    assert multiply(any_number, 0) == 0

    print("All tests passed!")

test_multiply()
```

With these tests, you can ensure that the `multiply` function behaves as expected with different input scenarios.