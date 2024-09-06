```python
def truncate_number(number):
    return number - int(number)
```

The `truncate_number` function takes a float number as input and returns the decimal part of the number by simply subtracting the integer part of the number, which can be accomplished by using the `int()` function that returns the integer value of the number, and the remainder becomes the decimal part, which is returned. The markdown code block above contains a Python script with a self-contained function that solves the problem and passes the test as described in the prompt. 

This solution is straightforward and effective in returning the desired decimal part. 

You can verify the correctness of the solution by calling the function with the example provided in the prompt: 
```python
>>> truncate_number(3.5)
0.5
```
This will return 0.5, which is the decimal part of the number 3.5.