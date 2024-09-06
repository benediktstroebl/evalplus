```python
def count_nums(arr):
    output = sum(int(n) for n in arr if sum(int(d) for d in str(n)) > 0)
    return output
```
This function uses a generator expression that iterates through each element in the input array `arr`. It converts each element to an integer using `int(n)` and then converts it to a string using `str(n)`. It then iterates through each digit of the string version of the number, and calculates the sum of these digits using `sum(int(d) for d in str(n))`. Finally, it returns the count of numbers whose digit sum is greater than 0. 

Here is a test case to test the function:
```python
def test_count_nums():
    # Empty list
    assert count_nums([]) == 0

    # List with positive and negative numbers
    assert count_nums([-1, 11, -11]) == 1

    # List with identical numbers
    assert count_nums([1, 1, 2]) == 3

    # List with single number
    assert count_nums([123]) == 1
```
This test script checks the function against several different inputs to verify that it behaves as expected. In particular, it checks that the empty set returns 0, that both positive and negative numbers are counted correctly, and that multiple identical numbers are correctly identified.