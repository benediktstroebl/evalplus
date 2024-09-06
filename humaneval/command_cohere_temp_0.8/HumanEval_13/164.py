```python
def greatest_common_divisor(a, b):
    """ Returns the greatest common divisor of two integers a and b """
    if a == 0:
        return b
    return greatest_common_divisor(b%a, a)
```
This recursive approach to finding the greatest common divisor is very efficient and idiomatic in Python. The time complexity is logarithmic (O(log(min(a, b))). This is achieved by taking advantage of the intrinsic link between recursion and division/modulo in division rings. 

It is also worth noting that Python and many other programming languages provide a built-in `math.gcd` function that performs this same task, but this is often faster due to avoiding extraneous overhead.

This problem can also be solved using iterators and generators, which is a more declarative approached geared towards deep composability. This is one way to solve the problem in Haskell, for example:
```haskell
gcd :: Int -> Int -> Int
gcd a0 b0 =
  let gcd a b | a == 0 = b
              | otherwise = gcd b (a `mod` b)
  in  gcd a0 b0
```
However, the recursive approach is more direct and often faster in Python, due to the overhead of generators and the call stack.