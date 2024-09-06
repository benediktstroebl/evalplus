Here's a Python script that contains a function called `even_odd_palindrome` which takes in a positive integer `n` and returns a tuple with the count of even and odd integer palindromes in the range from 1 to `n` (inclusive):
```python
def even_odd_palindrome(n):
    even, odd = 0, 0
    for i in range(1, n + 1):
        if str(i) == str(i)[::-1]:
            if i % 2 == 0:
                even += 1
            else:
                odd += 1
    return (even, odd)
```

The function counts the number of even and odd-numbered palindromes in the range from 1 to `n` (`inclusive`), then returns them as a tuple (`even`, `odd`). While looping through the numbers from `1` to `n`, it checks if each number is a palindrome by converting it to a string and comparing it to its reverse (`str(i) == str(i)[::-1]`). If it is a palindrome, it checks its parity (`i % 2 == 0`) and updates the appropriate count. The base case loops from `1` to `n` as both odd and even palindromes include `1` whereas the odd palindrome excludes `2`. 

The best efficiency we can achieve is O(n), since we have to iterate through all the numbers to count the odd and even palindromes.  This is the runtime complexity of the fastest possible algorithm for this specific problem.