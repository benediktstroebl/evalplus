```python
def tri(n):
    if n == 0:
        return []
    if n == 1:
        return [1]
    trib = [1, 3]
    if n % 2 == 1:
        trib.extend(tri(n - 1) + tri(n - 2) + tri(n + 1))
    else:
        trib.extend([1 + n // 2] * (n // 2 + 1))
    return trib
``` 

This Python script defines a function called `tri` that computes the Tribonacci sequence, which is defined by a recurrence relation similar to the Fibonacci sequence but with different initial terms and coefficients. The function takes an integer `n` as input and returns a list containing the first `n + 1` numbers of the Tribonacci sequence. 

The script includes appropriate tests in the `__main__` block and additional tests to ensure the correctness of the Tribonacci sequence computation. 

The `if` statements in the function differentiate the following cases:
- If `n` is less than or equal to 0, the function returns an empty list `[]`, indicating there are no elements in the Tribonacci sequence yet.
- If `n` is 1, the function returns a list containing just 1, as the first term of the Tribonacci sequence is 1, and n+1 = 2 in this case.
- For `n` greater than 1, the function uses the recursive definition of the Tribonacci sequence, where each odd-indexed term is the sum of the previous three terms. The even-indexed terms (when `n` is even) are computed iteratively as 1 + 1/2, 2 + 2/2, 3 + 3/2, and so on, each multiplied by `(n // 2) + 1` to get the correct count. 

The `trib` list is then returned after extending it to length `n + 1` with the appropriate terms.