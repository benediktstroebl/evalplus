```python
def reverse_delete(s, c):
    # Remove characters in c from s
    s = [i for i, char in enumerate(s) if char not in c]

    # Check for palindrome
    return (''.joinjoin(s), False)

# Test cases
test_cases = [
    ("abcdef", "b"),  # acdef, False
    ("abcdedcba", "ab"),  # cdedc, True
    ("abcde", "a"),   # abcde, False
]

for s, c in test_cases:
    result = reverse_delete(s, c)
    print(f"Input: {s}, Character set: {c}, Result: {result}, Palindrome: {result[1]}")
```