Here's a Python script that solves the problem:
```python
def decimal_to_binary(decimal):
    """Convert a decimal number to binary format."""
    db_prefix = "db"
    db_suffix = "db"
    binary_string = "{0:b}".format(decimal)
    return db_prefix + binary_string + db_suffix
```
This code uses the format method to convert the decimal number to a binary string. The binary string is then prepended and appended with 'db' to ensure the required output format.