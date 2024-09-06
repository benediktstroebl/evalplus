```python
def truncate_number(number: float) -> float:
    return number - int(number)
```
This function simply subtracts the largest integer less than number from number, which is the basic definition of the decimal part of a number. 

To test this function, you can call it with a floating point input like 3.5 and verify that the output is 0.5. 

This approach is straightforward and efficient, providing a clear and concise solution to the problem statement. 
```python
test_truncate_number = 3.5
expected = 0.5
result = truncate_number(test_truncate_number)

if result == expected:
    print("pass")
else:
    print("fail")
``` 
The test code provided can be used to verify the correctness of the solution in the context of the given problem.