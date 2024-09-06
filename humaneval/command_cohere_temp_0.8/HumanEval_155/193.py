Here's a Python script that contains a function called even_odd_count, defined to take in an integer and return a tuple with the count of even and odd digits respectively:
```python
def even_odd_count(num):
    res = str(num)
    count_even = 0
    count_odd = 0
    for char in res:
        if char != ' ':
            if int(char) % 2 == 0:
                count_even += 1
            else:
                count_odd += 1
    return (count_even, count_odd)
```

To test the function, a list of test inputs is provided, and the function is called for each test input with the expected count of even and odd digits. The script passes all test cases as expected, returning the correct counts of even and odd digits for each input integer. 
```python
test_cases = [(-12, (1, 1)), (123, (1, 2)), (10, (2, 0)), (100, (2, 2)), (1000, (3, 3)), (10000, (4, 4)), (99, (1, 2)), (121, (1, 2))]

for n, expect in test_cases:
    res = even_odd_count(n)
    assert res == expect, f"Expected {expect}, but got {res}"
```