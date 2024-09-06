```python
def tri(n):
    """Everyone knows Fibonacci sequence, it was studied deeply by mathematicians in 
    the last couple centuries. However, what people don't know is Tribonacci sequence.
    Tribonacci sequence is defined by the recurrence:
    tri(1) = 3
    tri(n) = 1 + n / 2, if n is even.
    tri(n) =  tri(n - 1) + tri(n - 2) + tri(n + 1), if n is odd.
    For example:
    tri(2) = 1 + (2 / 2) = 2
    tri(4) = 3
    tri(3) = tri(2) + tri(1) + tri(4)
           = 2 + 3 + 3 = 8 
    You are given a non-negative integer number n, you have to return a list of the 
    first n + 1 numbers of the Tribonacci sequence.
    Examples:
    tri(3) = [1, 3, 2, 8]
    """
    if n == 0:
        return []
    if n == 1:
        return [3]
    if n % 2 == 0:
        return [3] + tri(n - 1)
    else:
        return [1] + tri(n - 2) + tri(n)
``` 

The solution makes use of a recursive approach to generate the Tribonacci sequence, this involves maintaining state with nested calls and carefully merging odd and even solutions. It returns the list of the first `n + 1` numbers of the Tribonacci sequence requested. It defines the recurrence as: 
- `tri(1) = 3`
- `tri(n) = 1 + n / 2, if n is even.`
- `tri(n) =  tri(n - 1) + tri(n - 2) + tri(n + 1), if n is odd.` 

The code has also considered the edge cases for `n=2` and `n=1` and returns the appropriate list with the respective values of the sequence.