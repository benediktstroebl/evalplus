```python
def choose_num(x, y):
    max_even = -1
    temp_num = x
    check_even = 2
    
    while temp_num <= y:
        if temp_num % 2 == 0:
            if max_even < temp_num:
                max_even = temp_num
        temp_num += 1
    
    if max_even == -1:
        return -1
    else:
        return max_even
```
This Python script defines a function choose_num(x, y) that takes two positive numbers x and y as arguments and returns the largest even integer that falls within the range [x, y], inclusive. If no such even number is found within this range, it returns -1. The code employs a while loop to examine numbers incrementally within the specified range, tracking the largest even number encountered (`max_even`). The loop incrementally increases the variable temp_num from x to y, checking if each number is even (using the condition `temp_num % 2 == 0`). If the number is even, it compares it to the current maximum even number, updating `max_even` if a larger even number is found. The loop continues until temp_num exceeds y. If no even number is encountered within the range, max_even remains -1, and the function returns -1 to indicate the absence of an appropriate even number. Otherwise, it returns the largest even number found. 

Here is an example of how to use the function:
```python
answer = choose_num(12, 15)
print(answer)  # Output: 14
```
This calls the function with the arguments 12 and 15, and the function returns the number 14 which is the largest even number in the range and prints out the result. 

And here is another example:
```python
answer = choose_num(13, 12)
print(answer)  # Output: -1
```
This calls the function with the arguments 13 and 12, and the function returns the number -1 which is being returned when there is no largest even number in the range and prints out the result.