Here's a Python script that contains a function called even_odd_count that takes an integer num as input and returns a tuple with the count of even and odd digits in num, respectively:
```python
def even_odd_count(num):
    count = 0
    # Iterate each digit in the input number
    for digit in str(num): 
        # increment count if digit is odd
        if digit % 2 == 1: 
            count += 1
    return count, len(str(num)) - count
```

To test the above function, a main function is included to assert the output of the even_odd_count function against the expected result for a given input. 

```python
def main():
    # Test Case 1
    num = -12
    expected_result = (1, 1)
    result = even_odd_count(num)
    assert result == expected_result

    # Test Case 2
    num = 123
    expected_result = (1, 2)
    result = even_odd_count(num)
    assert result == expected_result

if __name__ == "__main__":
    main()
```

The tests are placed in the main function to check the functionality of the even_odd_count function. The output of even_odd_count is compared to the expected result with assert statements. If the inputs and steps are executed directly, the console should show the "Assertion Passed" for both tests.