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

The function `choose_num()` takes two parameters, `x` and `y`, and searches for the biggest even integer that exists in the range between them. It uses a `while` loop to iterate through the numbers starting from `x` and finishing at `y`, or `temp > y`, whichever occurs first. The loop checks for evenness using the modulo operator `%` with 2, and if the number is even, it becomes the `max_even` variable, which is later returned. The loop increments the variable `temp` by 1 on each iteration, which acts as a progression through the numbers. The `-1` value is returned if no even number is found within the range. 

This solution is efficient and adaptable to different ranges, making it useful for scenarios where a ceiling value might be imposed on an even number. 

To demonstrate the function, here is a test drive function for it:
```python
def test_choose_num():
    assert choose_num(12, 15) == 14
    assert choose_num(13, 12) == -1
    assert choose_num(2, 10) == 8
    assert choose_num(100, 200) == 198

test_choose_num()
```

This would help verify that the function behaves as expected. 
The test drive function calls the `choose_num()` function with different input arguments and checks for the expected output. 
The assert statements will cause the test drive function to fail if the `choose_num()` function does not produce the expected results. 

You can use this self-contained Python script to solve the original problem and to test the function.  You can also adapt it to suit your needs or further refine its behavior.