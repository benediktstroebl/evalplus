```python
def truncate_number(n):
    # We split the number into integer part and fractional part
    i, f = divmod(n, 10)

    # return fractional part of the number
    return f
```
This Python code defines a function called `truncate_number` that takes an input parameter `n`. The function effectively splits the input number into an integer part and a fractional part. It utilizes the use of the `divmod()` function to extract the integer part and fractional part of the input number by dividing it by 10 and taking the quotient and remainder, respectively. It then returns the the fractional part of the number, which represents the leftover part after removing the largest decimal digits from the input number.