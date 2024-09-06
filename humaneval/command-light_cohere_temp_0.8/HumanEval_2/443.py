```python
def truncate_number(number: float) -> float:
    return 0.5 if number < 0.1 else (number //float(str[int(number)] + '0' * (number < 0) - 1)))

# Example usage
n = 3.5
print(f"The decimal part is: {truncate_number(n)}")  # Output: 0.5
```
This Python function, `truncate_number`, takes a single parameter, `number: float`, which is expected to be a positive floating point number. The function then checks whether `number` is less than `0.1` or if this to the condition, it returns the decimal part of the number, which is the integer part of the number less than `1` and multiplied by `10` to remove the decimal portion. If `number` is not less than `0.1`, the using the other case, it returns the result of `number.float(str[int(number)] + '0' * (number < 0) - 1))`, which converts the number to a string and then extracts the integer part from it. The remaining decimal part of the number is then returned.