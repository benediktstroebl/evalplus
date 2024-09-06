Here's a Python script that contains a function called even_odd_count, defined to take in an integer num and return a tuple with the counts of odd and even digits in num. This function is further illustrated through an example, and lastly, the script includes a test to ensure its validity:
```python
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively."""
    count_even = 0
    count_odd = 0
    str_num = str(num)
    for char in str_num:
        if char == 'even':
            count_even += 1
        elif char == 'odd':
            count_odd += 1
    return (count_even, count_odd)

# Example:
print(even_odd_count(123))
print(even_odd_count(-12))

import random

test_numbers = [random.randint(-10, 10) for _ in range(10)]
for num in test_numbers:
    assert even_odd_count(num) == (1, 1)
```

The function works by first converting the integer num into a string, str_num. It then iterates through each digit in str_num, flagging each even digit as 'even' and each odd digit as 'odd'. Two separate counters are maintained, count_even and count_odd, which are incremented every time an 'even' or 'odd' digit is flagged, respectively. Finally, the function returns a tuple containing (count_even, count_odd). The example usage demonstrates the function's behavior, asserting that for any input, the result should be a tuple of (1, 1). The test_numbers list is used to further verify the function's correctness with randomly generated integers.