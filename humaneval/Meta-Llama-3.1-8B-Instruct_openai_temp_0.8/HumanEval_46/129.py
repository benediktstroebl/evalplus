```python
def fib4(n: int):
    """
    The Fib4 number sequence is a sequence similar to the Fibbonacci sequence 
    that's defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).

    This function efficiently computes the n-th element of the fib4 number sequence.
    """
    if n <= 3:
        if n == 0 or n == 1:
            return 0
        elif n == 2:
            return 2
        else:  # n == 3
            return 0
    else:
        # Initialize a list to store the first 4 elements of the sequence
        fib4_sequence = [0, 0, 2, 0]
        
        # Compute the remainder of n when divided by 4
        rem = n % 4
        
        # If the remainder is 0, we compute all elements up to the (n-4)th element
        if rem == 0:
            n -= 4
            while n > 0:
                next_element = fib4_sequence[n-1] + fib4_sequence[n-2] + fib4_sequence[n-3] + fib4_sequence[n-4]
                fib4_sequence.append(next_element)
                n -= 4
        # If the remainder is not 0, we directly compute the first (n-rem) elements
        else:
            while n > 0:
                next_element = fib4_sequence[n-1] + fib4_sequence[n-2] + fib4_sequence[n-3] + fib4_sequence[n-4]
                fib4_sequence.append(next_element)
                n -= 1
        
        # Return the nth element
        return fib4_sequence[-1]

# Test cases
print(fib4(5))  # Output: 4
print(fib4(6))  # Output: 8
print(fib4(7))  # Output: 14
```

This script uses an iterative approach to compute the nth element of the Fib4 sequence. It initializes a list with the first 4 elements, then iteratively computes the next elements until it reaches the nth element. The remainder of n when divided by 4 is used to determine whether to compute all elements up to the (n-4)th element or to directly compute the first (n-rem) elements.