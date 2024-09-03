```python
def decimal_to_binary(n): 
    return "db" + bin(n)[2:].z + "db"

def test_decimal_to_binary():
    assert decimal_to_binary(15) == "db1111db"
    assert decimal_to_binary(32) == "db100000db"
    assert decimal_to_binary(0) == "dbb0db"
    assert decimal_to_binary(-5) == "dbbeedbb0db"
    assert decimal_to_binary(12345) == "dbbed000db"
```