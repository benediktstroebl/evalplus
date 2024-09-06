```python
def string_sequence(n: int) -> str:
    return f"0 {n}:{n+1}"[:n+1]

# Test cases
test_seq = []
for i in range(10): 
    test_seq.append(string_sequence(i))

print(test_seq)
```