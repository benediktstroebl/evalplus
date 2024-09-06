Here's a Python script that contains a function called `even_odd_palindrome` which takes in a positive integer `n` and returns a tuple with the count of even and odd integer palindromes in the range from 1 to `n` inclusive. The function relies on a helper function called `is_palindrome` to determine if a number is a palindrome:
```python
def is_palindrome(num):
    """
    Helper function to determine if a number is a palindrome.
    Args:
        num (int): Number to be checked
    
    Returns:
        bool: True if the number is a palindrome, False otherwise
    """
    return str(num) == str(num)[::-1]

def even_odd_palindrome(n):
    """
    Given a positive integer n, return a tuple that has the number of even and odd
    integer palindromes that fall within the range(1, n), inclusive.
    Args:
        n (int): Positive integer container expects
    
    Returns:
        tuple: A tuple containing (count of even palindromes, count of odd palindromes)
    """
    even_count, odd_count = 0, 0
    for num in range(1, n+1):
        if is_palindrome(num):
            if num % 2 == 0:
                even_count += 1
            else:
                odd_count += 1
    return (even_count, odd_count)
```

The `is_palindrome` function is a simple helper function that checks if a given number is a palindrome by comparing its digits from the beginning and end and returning `True` if they are the same. In the `even_odd_palindrome` function, we iterate through the range from 1 to `n` and check each integer to see if it's a palindrome using the `is_palindrome` helper. We then classify each palindrome as either even or odd and increment the respective count. Finally, the function returns a tuple containing the counts of even and odd palindromes. 

This approach allows the code to achieve the intended functionality in a concise and scalable manner.