Here's a Python script with a self-contained function that returns a string containing space-delimited numbers starting from 0 up to 20:
```python
def string_sequence(n: int) -> str:
    return ' '.join(str(i) for i in range(n))

# Test cases
test_seq = []
for i in range(1, 30):
    test_seq.append(string_sequence(i) + ' ')

# Print the test cases
print(*test_seq)

# Run the function and compare with test cases
result = string_sequence(30)
print(result, 'vs', end=' ')
for i, a in zip(test_seq, result. print + ['']):
    print(i, end=' ')
```