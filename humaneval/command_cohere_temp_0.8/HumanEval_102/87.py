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

The function `choose_num()` takes two parameters, `x` and `y`, and searches for the biggest even integer that lies in the inclusive range `[x, y]`. It initializes `max_even` with -1, which serves as a convenient default value to ensure that the function will return -1 if no suitable even number is found. 

The function then iterates through the range `[x, y]` using a while loop, evaluating whether each number is even (i.e., divisible by 2 without a remainder). If a number is even, it updates `max_even` with that number. The loop continues until the end of the loop, where the variable `temp` exceeds the value of `y`. 

If the loop completes without finding a even number in the range, the `max_even` variable will still have the initial value of -1, which indicates no suitable even number was found. Hence, the function returns -1 in such cases. 

This approach ensures that the code is efficient in both time and space as it only needs to iterate through the necessary values once, without storing any additional data.