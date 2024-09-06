```python
def sort_even(l):
    even, odd = zip(*[iter(l)]*2)
    return list(odd)+list(sorted(even))
```
This solution utilizes the method of vectorization, created lists even and odd, which zip together, the odd indices and even indices of the input list l, respectively. The solution then uses the constructor list to convert the two generators into actual lists, which are concatenated and returned. Thanks to the recent improvements in Python generation expressions, this solution is shorter and more concise, while remaining readable and adhering to Python syntax standards.