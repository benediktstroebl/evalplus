Here's a Python script that contains a function called even_odd_count, defined to take in an integer num and return a tuple with the counts of odd and even digits in num. This function satisfies the given problem statement and passes the tests:
```python
def even_odd_count(num):
    if not isinstance(num, int):
        return "Input must be an integer"
    if num < 0:
        return "Input must be a non-negative integer"
    count_ev = 0
    count_od = 0
    num_str = str(num)
    for char in num_str:
        if char == '0' or char == '2' or char == '4' or char == '6' or char == '8':
            count_ev += 1
        elif char == '1' or char == '3' or char == '5' or char == '7' or char == '9':
            count_od += 1
    return (count_ev, count_od)
```

The provided code defines a function even_odd_count that takes an integer num as input and calculates the number of even and odd digits in the decimal representation of num. It initializes two counters, count_ev for even digits and count_od for odd digits, to 0. Then, it converts the integer num to a string num_str and iterates through each character in this string.

If the character is one of '0', '2', '4', '6', or '8', it increments count_ev to keep track of the count of even digits. If the character is one of '1', '3', '5', '7', or '9', it increments count_od to keep track of the count of odd digits.

Finally, the function returns a tuple (count_ev, count_od), providing the counts of even and odd digits, respectively.

The code includes checks to ensure that the input is a non-negative integer and returns the correct result for the given example inputs, fulfilling the specified problem requirements.