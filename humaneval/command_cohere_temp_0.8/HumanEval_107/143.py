Here's a Python script that contains a function called `even_odd_palindrome` that solves the problem you've described:
```python
def even_odd_palindrome(n):
    # Count even and odd length palindromes
    even_count = 0
    odd_count = 0
    
    for i in range(1, n+1):
        # Check if the reversed string is equal to the original string
        if str(i) == i[::-1]:
            if i % 2 == 0:
                even_count += 1
            else:
                odd_count += 1

    return (even_count, odd_count)
```

This function takes a positive integer `n` as input and returns a tuple with two elements: the first element represents the count of even-length integer palindromes in the range `[1, n]`, and the second element represents the count of odd-length integer palindromes in the same range. The function uses a loop to iterate through all numbers from 1 to `n` and checks if each number is a palindrome by comparing the string representation of the number with its reverse using slicing. If it's a palindrome and the number is even, it adds 1 to the even count; otherwise, it adds 1 to the odd count. The function ensures that it handles both even and odd-length palindromes correctly while counting.