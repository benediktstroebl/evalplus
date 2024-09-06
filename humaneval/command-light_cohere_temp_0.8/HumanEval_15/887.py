```python
def string_sequence(n: int) -> str:
    return f"0 {n}" * (n+1)

def test_sequence(n: int) -> None:
    assert str(string_sequence(n)) == f"0 {n}", f"Error: {n} should give '{0 {n}' but got {input}"
    return_str

n = int(input("Enter a number: "))
test_sequence(n)
print("Passed test!")
```