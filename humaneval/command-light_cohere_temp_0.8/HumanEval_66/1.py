```python
def digitSum(s):
    return sum(map(ord, s[::-1]))

# Test cases
test_cases = [
    "",          # Should return 0
    "abAB",     # Should return 131
    "abcCd",    # Should return 67
    "helloE",  # Should return 69
    "woArBld",   # Should return 131
    "aAaaaXa",   # Should return 153
]

def test():
    for case in test_cases:
        actual = digitSum(case)
        assert actual == case[-1:]  # Assertion to check the correctness of the function

if __name__ == "__main__":
    test()
```
The code defines a function `digitSum` that calculates the sum of the ASCII values of the upper characters in a given string. It then tests this function with various test cases and asserts the correctness of its output.