Here's a Python script that includes a function to solve the given problem:
```python
def count_palindromes(n):
    # Count even palindromes
    even = 0
    for i in range(1, n+1):
        if str(i) == str(i)[::-1] and i % 2 == 0:
            even += 1
    # Count odd palindromes
    odd = 0
    for i in range(1, n+1):
        if str(i) == str(i)[::-1] and i % 2 != 0:
            odd += 1
    return even, odd

# Example Usage
n = int(input())
even, odd = count_palindromes(n)
print(f"(Self-contained) Example 1: {even}, {odd}")
```

You can run this code and input an integer (n) to see the number of even and odd palindromes up to that number. Please note that this code handles the palindrome check and counting directly using Python's built-in features, as per the self-contained requirement.