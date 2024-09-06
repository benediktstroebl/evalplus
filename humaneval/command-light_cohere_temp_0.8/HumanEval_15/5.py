```python
def string_sequence(n: int) -> str:
    if n <= 0:
        raise ValueError("n should be a positive integer")
        
    result = ['0']
    for i in range(1, n+1):
        result.append(str(i))
    return '\n'.join(result)

# Test cases
test_cases = [0, 1, 10, 1337]
test_results = []
for n in test_cases:
    test_results.append(string_sequence(n))

# Print the results
for res in test_results:
    print(res)
```