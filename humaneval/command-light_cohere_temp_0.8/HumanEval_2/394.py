```python
def truncate_number(number: float) -> float:
    return 0.5 if number < 1 else:
        return number - 1  # Change based on original function
```
This function takes a floating point number as input and returns the decimal part of the number. It works by first checking if the input number is less than 1. If it is, it returns the original number. Otherwise, it subtracts 1 from the input number and returns the result.