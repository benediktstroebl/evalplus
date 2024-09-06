```python
def greatest_common_divisor(a, b):
    if not a or not b:
        return 0

    c = 0
    while b > 0:
        if a % b == 0:
            c += 1
            a //= b
        else:
            b = divmod(b, a)[1]

    return c

# Test case using markdown code block
3 #md} 5
{:}
(c) = greatest_common_divisor(3, 5)
{print(c)} # Output: 1

25 #md} 15
{:}
(c) = greatest_common_divisor(25, 15)
{print(c)} # Output: 5
```