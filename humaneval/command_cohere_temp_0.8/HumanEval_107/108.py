```python
def count_palindromes(n):
    # memoization for windowed palindrome count
    dp = [0] * (n + 1)
    dp[0] = dp[1] = 1

    for i in range(2, n + 1):
        if i == dp[i]:
            dp[i] += 1
        else:
            dp[i] = dp[i - 1]

    # even and odd counts
    even, odd = 0, 0
    for i in range(1, n + 1):
        if i == dp[i]:
            if i % 2 == 0:
                even += 1
            else:
                odd += 1

    return even, odd

n = int(input())
even, odd = count_palindromes(n)
print(f"(#{even}, #{odd})")
```

The `count_palindromes` function uses memoization to calculate the count of palindromes within a given range `1` up to `n` (`dp[i]`). Then, it separately calculates the count of even and odd palindromes by iterating through the `dp` array and checking if each palindrome is even or odd. 

The overall time complexity of this code is O(n). The space complexity is O(n) due to the existence of the `dp` array. 

This code is efficient and can effectively solve the even and odd palindrome count problem for inputs up to 1000.