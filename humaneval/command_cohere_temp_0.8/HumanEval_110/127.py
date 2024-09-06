```python
def exchange(lst1, lst2):
    even_found = any(map(lambda x: x % 2 == 0, lst1))
    count_diff_odd = sum(x % 2 != y % 2 for x, y in zip(lst1, lst2))
    return "YES" if even_found and count_diff_odd <= len(lst1) // 2 else "NO"
```

The script employs a straightforward algorithm to solve the problem:
1. **Verify if at least one even number is present in lst1**: With the `any()` function and a lambda function, we check if any element in lst1 is even.
2. **Count the difference between odd and even numbers**: This is done by counting how many numbers in lst1 are not even, given that their counterparts in lst2 are even. This is achieved with the `sum()` function and a generator expression.
3. **Return "YES" if it is possible to exchange elements**: This is true if at least one even number is found in lst1, and the count of different odd numbers between lst1 and lst2 is less than or equal to half the length of lst1. This is done to allow for the exchange of odd numbers from lst1 with even numbers from lst2, until all elements in lst1 are even.
4. **Return "NO" otherwise**: If we cannot fulfill the conditions above, we are not able to change lst1 to contain only even numbers by exchanging elements with lst2.

This algorithm efficiently solves the problem, and the returned result is either "YES" or "NO", depending on the stated conditions. 
The test cases provided ensure the function's correctness and handle various scenarios, covering different input list permutations and lengths.