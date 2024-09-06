```python
def exchange(lst1, lst2):
    odd = next((el for el in lst1 if el % 2 != 0), None)
    even = next((el for el in lst2 if el % 2 == 0), None)
    if odd is None or even is None:
        return "YES"
    return "NO"
```

The `exchange()` function takes two lists, `lst1` and `lst2`, and returns "YES" if it's possible to exchange elements between them so that `lst1` contains only even numbers. Otherwise, it returns "NO". The function utilizes the next() method to find the first odd number in `lst1` and the first even number in `lst2`, determining the potential success of the exchange. If either an odd number or an even number is not found, indicating at least one even number in `lst1` or an odd number in `lst2`, "YES" is returned. Feel free to add more cases to the tests to cover other scenarios.  This approach doesn't require mutating the original lists, ensuring that the solution is efficient and non-destructive.  This problem can be solved in many other creative ways, using recursion, filtering techniques, or other methods.