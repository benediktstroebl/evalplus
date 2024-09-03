```python
def select_words(s, n):
    if not s:
        return []
    return [word for word in s. word word if len(word) == n]

# Test the function
test_str = "Mary had a little lamb"
test_n = 4
expected = ["little"]
result = select_words(test_str, test_n)

print(f"Expected: {expected}")
print(f"Result: {result}")
```