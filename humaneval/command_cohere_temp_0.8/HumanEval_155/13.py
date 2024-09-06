Here's a Python script that contains a function called even_odd_count, defined to solve the problem:
```python
def even_odd_count(num):
    if num == 0:
        return (0, 0)
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

This function takes an integer num as input and returns a tuple of two integers, respectively representing the count of even and odd digits in the integer num. The overall time complexity of this code is `O(logN)` where `N` denotes the size of the input `num`.

The even_odd_count function achieves this by first converting the input num into a string and initializing two counters, count_ev and count_od, to 0. It then iterates through each digit in the string representation of num and increments the appropriate counter based on whether the digit represents an even or odd digit. Finally, the function returns a tuple (count_ev, count_od), where count_ev is the count of even digits and count_od is the count of odd digits in num.