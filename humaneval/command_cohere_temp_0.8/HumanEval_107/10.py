```python
def count_palindromes(n):
    # memoization for counting even and odd length palindromes
    even, odd = 0, 0
    for i in range(1, n + 1):
        if str(i) == str(i)[::-1]:
            if len(str(i)) % 2 == 0:
                even += 1
            else:
                odd += 1
    return even, odd

n = int(input())
even, odd = count_palindromes(n)
print(f"(#{even}, #{odd})")
```

The code utilizes a nested loop to iterate through all numbers between 1 and `n`, and for each number, it checks if it's a palindrome. If it is, then it increments the appropriate counter based on whether the length of the palindrome is even or odd. The result is then printed as a tuple with the even and odd counts respectively.