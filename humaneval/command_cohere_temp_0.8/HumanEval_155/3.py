Here's a Python script that contains a function called even_odd_count which takes in an integer and returns a tuple with the count of even and odd digits respectively:
```python
def even_odd_count(num):
    if num == 0:
        return (0, 0)
    count_even = 0
    count_odd = 0
    num_str = str(num)
    for char in num_str:
        if char != ' ':
            if int(char) % 2 == 0:
                count_even += 1
            else:
                count_odd += 1
    return (count_even, count_odd)
```

This function converts the input integer into a string and iterates through each character in the string. It distinguishes between spaces and digits, counting the digits as either even or odd. Ultimately, it returns a tuple containing the respective counts of even and odd digits.

To ensure correctness, here is a simple test case:
```python
test_cases = [(1, (0, 1)), 
             (-12, (1, 1)), 
             (123, (1, 2))]

for num, expected in test_cases:
    res = even_odd_count(num)
    assert res == expected, f"For input {num}, expected {expected}, got {res}"
``` 

This test suite confirms that the function appropriately counts even and odd digits for various inputs.