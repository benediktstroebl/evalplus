Here's a Python script that contains a function called even_odd_count, defined to solve the problem you've described:
```python
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively."""
    count_even = 0
    count_odd = 0
    temp_num = abs(num)
    while temp_num != 0:
        digit = temp_num % 10
        if digit % 2 == 0:
            count_even += 1
        else:
            count_odd += 1
        temp_num //= 10
    return (count_even, count_odd)
```

This script defines a function even_odd_count that takes a single argument, num, and returns a tuple with two elements: count_even (the number of even digits) and count_odd (the number of odd digits). 

The function first sets the variable temp_num to the absolute value of num, and initializes count_even and count_odd to 0. It then enters a loop where it repeatedly divides temp_num by 10 and extracts the last digit using the modulo operator (%). If the digit is even, it increments count_even; otherwise, it increments count_odd. The loop continues until temp_num becomes 0.

The implementation is efficient because it progressively extracts the digits from the least significant digit (LSD) to the most significant digit (MSD) of temp_num, and at each step, it determines whether the digit is even or odd. 

The total time complexity is O(logN), where N is the number represented by num. 

The space complexity is also efficient, O(1), since only a constant number of variables are used.