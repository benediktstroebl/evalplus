Here's a Python script with a self-contained function that solves the problem:
```python
def modp(n, p):
    return (1 << n) % p

# Tests
n, p = 3, 5
print(f"{n=}, {p=}, {modp(n, p)=}")
assert modp(n, p) == 3

n, p = 1101, 101
print(f"{n=}, {p=}, {modp(n, p)=}")
assert modp(n, p) == 2

n, p = 0, 101
print(f"{n=}, {p=}, {modp(n, p)=}")
assert modp(n, p) == 1

n, p = 3, 11
print(f"{n=}, {p=}, {modp(n, p)=}")
assert modp(n, p) == 8

n, p = 100, 101
print(f"{n=}, {p=}, {modp(n, p)=}")
assert modp(n, p) == 1
```

This code defines a function `modp` that computes `2^n mod p` directly, where `n` and `p` are input arguments, and then it uses that function to solve the specific problem given various test cases. 

Please note that the markdown code block provided in the initial request was not formatted properly. If you would like the response to adhere to the exact formatting, I'll be more than happy to modify it accordingly. Feel free to ask if you have any further questions or if you'd like additional explanations.