```python
def f(n):
    facts = [0] * n
    sums = [0] * n
    for i in range(1, n+1):
        facts[i] = facts[i - 1] * i
        if i % 2 == 0:
            sums[i] = sums[i - 1] + i
    return facts + sums
```
This Python script defines a function 'f' that takes an input 'n', and returns a list according to the specification. The function first creates two lists, 'facts' and 'sums', each of size 'n', and initializes each element of these lists to 0. It then iterates through the range from 1 to 'n', calculating the factorial of even numbers and the sum of numbers from 1 to the current number for all numbers less than or equal to 'n'. The result is a list where the even indices hold the factorials and the odd indices hold the sums, which is achieved by concatenating the 'facts' and 'sums' lists.