```python
def truncate_number(number: float) -> float:
    return number - int(number)
```
This function simply subtracts the largest integer that is less than the input number from the input number, which yields the desired decimal part. 

To test this script, you can call the function with the example provided in the prompt, and compare the output to the expected result: 
```python
truncate_number(3.5)  # Expected output: 0.5
``` 
The output will be `0.5`, which is the same as the expected output. 

If you want to test more cases, you can add additional inline tests like this one with the `>>>` prompt operator, which evaluates expressions in the Python interpreter and prints the result, or you can create more comprehensive tests by developing a full test suite with `pytest`. 

Let me know if you need help with that! Or if you'd like to practice another way to solve this (agile) coding problem, providing a chance to discuss different approaches to a problem is an excellent way to gain experience and confidence in problem-solving!