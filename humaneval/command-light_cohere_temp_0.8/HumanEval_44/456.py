```python
def change_base(x: int, base: int) -> str:
    if not isinstance(x, int) or not isinstance(base, int):
        raise TypeError("Input must be of type int")
    if base < 2 or base > 36:
        raise ValueError("Base must be between 2 and 36")
        
    str_rep = ""
    while x > 0:
        str_rep = str(x % base) + str_rep
        x //= base
        
    return str_rep

# Test suite
test_change_base = [
    [
        {"Input": 8, "Base": 3},
        {"Should return": "'22'},
        {
            "Error": False
        }
    ]
, "test_change_base")

result = change_base(test_change_base[1], test_change_base[2])

print("Result:", result)

test_change_base[3]["Error"] == False
```