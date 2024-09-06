Here's a Python script that contains a function named `even_odd_palindrome` which addresses the problem you've outlined
```python
def even_odd_palindrome(n):
    even, odd = 0, 0
    for i in range(1, n+1):
        if str(i) == str(i)[::-1]:
            if i % 2 == 0:
                even += 1
            else:
                odd += 1
    return (even, odd)
```

The function uses a loop to iterate through all numbers from 1 to `n` and counts the numbers that are palindromes, incrementing a respective counter (`even` or `odd`) depending on whether the number is even or odd. The final count is returned as a tuple.

To ensure efficiency, let's analyze the time complexity of the given code
```python
def even_odd_palindrome(n):
    even, odd = 0, 0
    for i in range(1, n+1):
        if str(i) == str(i)[::-1]:
            if i % 2 == 0:
                even += 1
            else:
                odd += 1
    return (even, odd)
```

The time complexity is O(n). This is because the loop iterates over each number from 1 to `n` once, performing a constant-time operation to check if it's a palindrome and incrementing a counter based on its parity. Thus, for each additional integer `n`, the algorithm requires `O(1)` additional time. So the total time complexity is the sum of these constant times, which is `O(n)`.