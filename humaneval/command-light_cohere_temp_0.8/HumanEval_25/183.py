```python
def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(1097)
    []
    >>> factorize(59)
    []
    """
    
    prime = []
    for i in range(1,int(n**0.5)+1):
        if n%i == 0:
            prime.append(i)
            n//=i 
    return prime
``` 
The function uses trial and error approach to find prime factors of the number. It loops from the time up to the square root of the number and checks for each number till it reaches the square root. 
The function then returns a list of prime factors.