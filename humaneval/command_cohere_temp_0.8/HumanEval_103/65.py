Here's a Python script that contains a function 'rounded_avg' that solves the problem:
```python
def rounded_avg(n, m):
    if n > m:
        return -1
    num = (n + m) // 2
    rounded_num = round(num)
    return bin(rounded_num)[2:]
```

The function uses arithmetic to compute the average of integers between 'n' and 'm', inclusive. It then rounds the average to the nearest integer and converts the result to binary. If 'n' is greater than 'm', the function returns -1 as stated in the prompt.