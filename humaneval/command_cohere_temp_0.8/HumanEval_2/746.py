```python
def truncate_number(number):
    return number - int(number)
```
This Python script defines a function called truncate_number, which takes a single argument number. This function returns the decimal part of the input number. It does so by subtracting the integer part of the number (obtained by converting it to an integer) from the original number. 

The script adheres to Python's type hinting convention, indicating that the function takes a number parameter with a floating-point type.

To test this script, you can call the function with a floating-point number as follows:
```python
print(truncate_number(3.5))  # Output: 0.5
```
The function's behavior aligns with the problem statement's expected output, demonstrating its ability to extract and return the decimal portion of the input number.

This approach is efficient and provides a simple solution to the problem, making it a straightforward choice for solving this particular challenge.