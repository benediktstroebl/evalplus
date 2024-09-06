Here's a Python script that contains a function called even_odd_count, defined to solve the problem:
```python
def even_odd_count(num):
    if num == 0:
        return (0, 0)
    count_even = 0
    count_odd = 0
    temp = str(num)
    for i in temp:
        if i > '9':
            pass
        elif i == '0':
            count_even += 1
        else:
            count_odd += 1
    return (count_even, count_odd)
```

This function takes a num arbitrator through a given example. It breaks down the problem into the following steps:
1. A check is made to see if the integer is 0, and if so, the function returns 0 for both counts.
2. The variable temp is used to convert the number to a string, and the loop iterates over each digit.
3. If the digit is greater than 9, the loop continues to the next digit.
4. If the digit is 0, the even count is increased by 1.
5. If the digit is between 1 and 8, the odd count is increased by 1.

Finally, the function returns a tuple with the even and odd counts, respectively.