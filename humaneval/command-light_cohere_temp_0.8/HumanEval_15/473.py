```python
def string_sequence(n: int) -> str:
    return f"0 {n} ".center(n)

for i in range(0,6):
    assert str(string_sequence(i)).strip() == '0'.center(i), '0')
    print(i, ":",end=''')
```