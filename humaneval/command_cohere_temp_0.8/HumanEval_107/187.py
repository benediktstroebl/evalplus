Here's a Python script that includes a function to solve the problem:
```python
def count_palindromes(n):
    # Count even and odd length palindromes
    even = 0
    odd = 0
    
    for i in range(1, n+1):
        s = str(i)
        if s == s[::-1]:
            if len(s) % 2 == 0:
                even += 1
            else:
                odd += 1
    
    return even, odd

# Example usage
n = int(input())
even, odd = count_palindromes(n)
print(f"(#{even}, #{odd})")

```

The `count_palindromes` function takes an integer `n` as input and uses a loop to iterate through all numbers between 1 and `n`. It converts each number to a string, checks if it's a palindrome, and increments the appropriate counter (`even` or `odd`) based on whether the length of the palindrome is even or odd. The example usage section takes a user input and calls the function with the input as `n` and prints the returned even and odd counts. The script achieves a time complexity of O(n), where n is the given input number, as it iterates through all numbers up to `n` once and performs constant-time operations for each iteration.