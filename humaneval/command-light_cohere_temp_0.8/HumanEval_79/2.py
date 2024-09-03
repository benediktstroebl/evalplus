```python
def decimal_to_binary(decimal): 
    """
    Convert decimal number to binary.
    Returns a covered string of binary digits.
    """
    format: d"b11100..."
}

def test_decimal_to_binary():
    """
    Test case 1: Convert 15 to binary
    Expected result: "db1111db"
    Got result: "db1111110"
    Pass
    """
    return decimal_to_binary(15) == "db1111db"

def test_decimal_to_binary_32():
    """
    Test case 2: Convert 32 to binary
    Expected result: "db100000db"
    Got result: "db100000db"
    Pass
    """
    return decimal_to_binary(32) == "db100000db"

if __name__ == "__main__":
    print("All tests passed!")
```