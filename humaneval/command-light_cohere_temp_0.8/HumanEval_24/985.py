```python
def largest_divisor(n: int) -> int:
    """
    Returns the largest integer less than n, 
    that evenly divides n, i.it the nth_largest_divisor(n) which 
    is equal to n.
    """
    a function first computes the product of all 
    divisors of n, which is O(n^2), 
    using the formula n!/gcd(n,gcd(n,0)) (from
    the prime factorization). Then, 
    it uses the optimization technique to 
    only consider divisors larger than the 
    square root of n, which significantly reduces 
    the number of divisors to consider.
    """return n - maximum(n - 1, int(n**0.sqrt() + 2) // int(n**0.sqrt() -sqrt()))```