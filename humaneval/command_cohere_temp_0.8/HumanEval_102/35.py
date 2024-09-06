```python
def choose_num(x, y):
    max_even = -1
    temp_num = x
    while temp_num <= y:
        if temp_num % 2 == 0:
            max_even = temp_num
        temp_num += 1
    return max_even
```

The function `choose_num()` takes two parameters, `x` and `y`, and searches for the biggest even integer that exists in the range between `x` and `y`. It does so by initializing `max_even` to the value of -1, checking if each number in the range is even by using the modulo operator (`%`), and making sure the even numbers are progressively increasing until they reach the maximum even value. The function then returns the biggest even number found in the range, or -1 if no such number is found. 

Here is an example of how to use the above function:
```python
answer = choose_num(12, 15)
print(answer)
```

This will output:
```
14
```

This exemplifies how the function utilizes a loop and an if statement to efficiently identify the maximum even integer within the given range, making it easier to understand the logic behind the function.