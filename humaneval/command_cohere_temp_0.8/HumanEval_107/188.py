```python
def count_palindromes(n):
    # memoization
    count = {i: 0 for i in range(n + 1)}
    count[1] = 1

    for i in range(2, n + 1):
        if str(i) == str(i)[::-1]:
            count[i] = count[i - 1] + 1
        else:
            count[i] = count[i - 1]

    even, odd = 0, 0
    for i in range(1, n + 1):
        if count[i] % 2 == 0:
            even += count[i]
        else:
            odd += count[i]

    return even, odd

n = int(input())
even, odd = count_palindromes(n)
print(f'({even}, {odd})')
```

The way the code works is we initialize a dictionary, `count`, that will store the count of numbers up to `n` that are palindromes. We initialize the count of the number `1` to `1` since it is a palindrome. Then, we iterate through numbers `2` to `n` and check if the number is a palindrome. If it is, we increment the count of the previous number and the current number. If it is not, we only increment the count of the previous number. After that, we loop through the keys of `count` and separate even and odd palindrome counts and return them. We then take in `n` as an input, call our function, and print the results. 

The code manages to achieve a time complexity of O(n) through the use of memoization and linearly iterating through numbers up to `n`, and a space complexity of O(n) due to storing counts up to `n` in a dictionary. While this solution is straightforward and efficient, it lacks a more dynamic approach and does not leverage more advanced mathematical properties.