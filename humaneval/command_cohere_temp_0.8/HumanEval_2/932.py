```python
def truncate_number(number: float) -> float:
    return number - int(number)
```
This function simply subtracts the largest integer that is less than the input number from the input number, which yields the desired decimal part. 

To test this script, you can call the function with the example provided in the prompt, and compare the output to the expected output. 

To do so in the Python REPL:
```python
truncate_number(3.5)
```
This will return `0.5`, which is the expected output.