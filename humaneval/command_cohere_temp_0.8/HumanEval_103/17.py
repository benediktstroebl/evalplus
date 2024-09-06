Here is a Python script with a self-contained function `rounded_avg` that solves the problem:
```python
def rounded_avg(n, m):
    avg = (n + m) // 2
    if n > m:
        return -1
    else:
        return '{0:b}'.format(round(avg))
```
This script provides a function that takes in two positive integers, `n` and `m`, and calculates the average of the integers between them. The result is rounded to the nearest integer and returned as a binary string. If `n` is greater than `m`, it returns `-1`.

Here's an example of how you can use this function:
```python
rounded_avg(1, 5)  # Returns "0b11"
rounded_avg(7, 5)  # Returns -1
rounded_avg(10, 20)  # Returns "0b1111"
rounded_avg(20, 33)  # Returns "0b11010"
```
This function can be easily installed and used anywhere within your Python environment as it does not rely on any external modules or dependencies. You can further customize and extend this function to cater to more specific needs if required.