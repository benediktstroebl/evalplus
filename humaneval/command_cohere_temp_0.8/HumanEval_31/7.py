```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
```

This function adheres to the problem statement by determining a number's primality. It initiates by checking if the given number is less than 2, deeming such numbers as non-prime and exiting the function. The function then iterates through numbers from 2 up to the square root of the input number, checking for divisibility. If the number is divisible by any integer within this range, it is deemed non-prime and the function returns False. However, if the number is not divisible by any integer within this range, it is deemed prime and the function returns True. 

This function is efficient for its purpose, primarily employing linear time complexity in its iterations. It forms a foundational primality-checking function that can be applied in diverse contexts, including number theory, algorithm design, and computer science applications. 

The provided tests illustrate the function's correctness and inclusivity in handling diverse cases, assuring users of its reliability. This includes numbers referenced in edge cases, exceptional cases, and standards cases. 

This function can be applied to solve problems related to prime and composite numbers, and can also be modified to solve related problems, such as checking if a number is composite. 

It's noteworthy that this function excludes certain edge cases, including numbers with extensive digits ordeci/numeral systems beyond base 10. However, this can be rectified by modifying the function to handle such cases if needed.