Here's a Python script that contains a function called even_odd_count which takes an integer num as its input and returns a tuple with the counts of even and odd digits in num, as described in the problem:
```python
def even_odd_count(num):
    count_even = 0
    count_odd = 0
    num_str = str(num)
    
    # Iterate through each digit in the integer representation
    for digit in num_str:
        if digit % 2 == 0:
            count_even += 1
        else:
            count_odd += 1
    
    return (count_even, count_odd)

# Test Cases
assert even_odd_count(-12) == (1, 1)
assert even_odd_count(123) == (1, 2)
assert even_odd_count(15) == (1, 2)
```

This script defines the `even_odd_count` function, which takes an integer as input and returns a tuple of two counts: one for even digits and one for odd digits in the given number. The script then includes several test cases to verify the function's behavior against expected results.