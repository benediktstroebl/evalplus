```python
def sum_squares(lst):
    result = 0
    for n in lst:
        result += n**2
    
    return int(result)
```
The function `sum_squares` operates on a list of numbers, calculating the sum of squared integers therein. It does so iteratively, summing the squares of each number in the list using a loop. Importantly, before returning the computed sum, the function converts it to an integer type, ensuring the result is expressed as an integer value. 

This approach allows the function to handle various input scenarios, including both integer and float numbers, and delivers a concise, whole-number sum of the squared values, aligning with the problem's requirements. 

This code can be tested against the examples provided in the prompt, and all should return the expected output.