Here's a Python script that includes a function to solve the problem:
```python
def count_palindromes(n):
    # Count odd palindromes
    odd = 0
    for i in range(1, n+1):
        if str(i) == str(i)[::-1] and i%2:
            odd += 1
    # Count even palindromes
    even = 0
    for i in range(1, n+1):
        if str(i) == str(i)[::-1] and i%2 == 0:
            even += 1
    return even, odd

# Example usage
n = int(input())
even, odd = count_palindromes(n)
print(f"( #{even}, #{odd})")
```

You can call the `count_palindromes` function with an integer input `n`, and it will return a tuple containing the counts of even and odd palindromes within the range `[1, n]`. The example usage demonstrates this, printing the result as a tuple of numbers separated by commas.