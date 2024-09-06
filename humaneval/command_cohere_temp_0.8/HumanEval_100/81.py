```python
def make_a_pile(n):
    pile = [n]
    while len(pile) < n + 1:
        if n % 2 == 1:
            n += 2
        else:
            n += 1
        pile.append(n)
    return pile
```
This Python script defines a function named `make_a_pile` that solves the problem statement. Here's a breakdown:
1. The function takes a single argument `n`, which is the number of stones in the first level of the pile. 
2. It initializes a starter list called `pile` with the first level's stones (`n`).
3. A `while` loop is used to build the pile incrementally, adding one more stone each iteration until the pile's length reaches `n + 1`.
4. Within the loop, it checks whether `n` is odd or even to determine the next stone count:
   - If `n` is odd, it adds 2 to `n` to jump to the next odd number.
   - If `n` is even, it adds 1 to `n` to move to the next even number.
5. Regardless of the condition, it appends the new stone count to the `pile` list.
6. Once the loop completes, the function returns the `pile` list, which represents the number of stones in each level of the pile.

This solution is efficient and can solve the problem for any positive integer `n` in a single loop, making it an O(n) solution.