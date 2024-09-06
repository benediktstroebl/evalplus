```python
def count_palindromes(n):
    # memoization
    count = {i: 0 for i in range(1, n + 1)}
    count[1] = 1

    odd, even = 0, 0
    for i in range(2, n + 1):
        if i == int(str(i)[:::-1]):
            count[i] = count[i - 1] + 1
            if i % 2:
                odd += count[i]
            else:
                even += count[i]

    return even, odd

n = int(input())
even, odd = count_palindromes(n)
print(f"(:{even:^4}, {odd:^4})")
```

The `count_palindromes` function uses a dictionary to store the count of palindromes for each number between 1 and `n`. The dictionary is initialized so that `count[1] = 1` for the single palindromic number 1. The code then iterates through the range 2 to `n`, counting odd and even palindromes and updating the count for each number. The output is a tuple of the count of even and odd palindromes.  The program completes by prompting the user for an input integer `n`, calling `count_palindromes` and printing the result in the specified format.

This solution has a time complexity of O(n^2) due to the nested loop structure and the additional loop to count the palindromes. Nevertheless, it is feasible for the requested input range of 1 <= n <= 10^3.