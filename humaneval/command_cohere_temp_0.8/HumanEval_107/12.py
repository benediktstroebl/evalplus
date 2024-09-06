Here's a Python script that includes a function to solve the given problem:
```python
def count_palindromes(n):
    s = str(n)
    even, odd = 0, 0
    for i in range(len(s)//2):
        if s[i] == s[-1-i]:
            even += 1
        else:
            odd += 1
    return even, odd

def even_odd_palindrome(n):
    """
    Given a positive integer n, return a tuple that has the number of even and odd
    integer palindromes that fall within the range(1, n), inclusive.

    Example 1:

        Input: 3
        Output: (1, 2)
        Explanation:
        Integer palindrome are 1, 2, 3. one of them is even, and two of them are odd.

    Example 2:

        Input: 12
        Output: (4, 6)
        Explanation:
        Integer palindrome are 1, 2, 3, 4, 5, 6, 7, 8, 9, 11. four of them are even, and 6 of them are odd.

    Note:
        1. 1 <= n <= 10^3
        2. returned tuple has the number of even and odd integer palindromes respectively.
    """
    return count_palindromes(n)

# Test cases
print(even_odd_palindrome(3))
print(even_odd_palindrome(12))
```

This script defines a function `even_odd_palindrome` that takes in a positive integer `n` and returns a tuple of two values: the number of even and odd integer palindromes between 1 and `n` (inclusive). The function counts the number of characters in the string representation of `n` that are symmetric around its center. It treats these characters as odd palindromes and calculates the count. The rest are treated as even palindromes. The script also includes test cases to validate its functionality. 

Let's break down the `count_palindromes` function step by step:
1. **Function Definition**:
   ```python
   def count_palindromes(n):
       ...
   ```
   This defines a function named `count_palindromes` that takes a single argument `n`.

2. **String Conversion**:
   ```python
       s = str(n)
   ```
   The integer `n` is converted into a string `s`. This string representation is essential for palindrome detection.

3. **Even and Odd Variables**:
   ```python
       even, odd = 0, 0
   ```
   Two variables are initialized: `even` and `odd`. These will keep track of the count of even and odd palindromes, respectively.

4. **Palindrome Loop**:
   ```python
   for i in range(len(s)//2):
       ...
   ```
   A loop is initiated that iterates through each character in the string `s`. The `len(s)//2` is used to ensure the loop only iterates through the characters that fall in the center of the string (for detecting palindromes).

5. **Palindrome Detection**:
   ```python
       if s[i] == s[-1-i]:
           even += 1
       else:
           odd += 1
   ```
   Within the loop, it checks if the character at index `i` in the string `s` is the same as the character at index `−1-i` (which is the last character of the string). If they are the same, then it increments the count of even palind