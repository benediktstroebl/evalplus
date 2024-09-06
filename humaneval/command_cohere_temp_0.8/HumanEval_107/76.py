Here's a Python script that includes a self-contained function to solve the problem of counting even and odd integer palindromes within a given range:
```python
def even_odd_palindrome(n):
    even, odd = 0, 0
    for num in range(1, n + 1):
        reversed_num = int(str(num)[::-1])
        if num == reversed_num:
            if num % 2 == 0:
                even += 1
            else:
                odd += 1
    return (even, odd)
```

The function `even_odd_palindrome(n)` calculates the number of even and odd integer palindromes within the range `[1, n]`. It uses a loop to iterate through numbers from 1 to `n` and checks if each number is a palindrome by reversing its string representation and comparing it to the original number. If it is a palindrome, the function checks if it's even or odd and updates the respective count accordingly. The function then returns a tuple containing the counts for even and odd palindromes.