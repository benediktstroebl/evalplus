```python
def get_odd_collatz(n):
    odd_seq = [x for x in collatz_seq(n) if x % 2 == 1]
    odd_seq.sort()
    return odd_seq
    
def collatz_seq(n):
    if n == 1:
        return [1]
    else:
        seq = [n]
        while n != 1:
            if n % 2 == 0:
                n = n // 2
            else:
                n = 3 * n + 1
            seq.append(n)
        return seq

# Tests
assert get_odd_collatz(1) == [1]
assert get_odd_collatz(5) == [1, 5]
assert get_odd_collatz(12) == [1, 5, 11, 121]
``` 

This Python script defines a function `get_odd_collatz(n)` which returns a sorted list of odd numbers in the Collatz sequence of a given positive integer `n`. The Collatz sequence for a number is generated iteratively until it reaches the base case of `n == 1`. The generated sequence is then filtered to include only the odd numbers, and these odd numbers are sorted in ascending order. 

The unit tests demonstrated in the comment can be added to ensure the function's correctness. You can also add more tests to cover a variety of inputs.  This further demonstrates Python's practicality and flexibility in tackling and implementing mathematical and algorithmic problems like the Collatz sequence.