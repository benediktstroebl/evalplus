```python
def truncate_number(number):
    return number - int(number)
```

The `truncate_number` function takes a positive floating point number as input and returns the decimal part of the number. It does so by taking the difference between the given number and the closest integer (largest integer smaller than the given number) represented by the number, which effectively removes the integer part of the decomposition. 

Here is an example usage of the function:
```python
round_trip = 3.5
truncated = truncate_number(round_trip)
print(truncated)
```

This will print:
```
0.5
```

This output is the decimal part of the original number. 

The function's behavior aligns with the problem statement's expected output. However, it's important to note that the function assumes that the input is a positive floating point number and may not work as expected for other numeric types or negative numbers. 

To ensure robustness for all positive numeric inputs and negative numbers, you might consider using a more comprehensive check during the initialization of the function.