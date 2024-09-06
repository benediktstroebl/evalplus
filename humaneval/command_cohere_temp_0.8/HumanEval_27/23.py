```python
def flip_case(string: str) -> str:
    return ''.join(c.swapcase() if c.isalpha() else c for c in string)
```

This code uses the swapcase function to convert all characters to their flip case counterparts, but it also correctly handles non-alphabetic characters by bypassing the swapcase function for non-alphabetic characters. As a result, the code ensures that punctuation and other non-alphabetic characters are left unchanged. 

Here is an example usage of this code:
```python
print(flip_case("Hello, World!"))  # Outputs: "hELLO, wORLD!"
```

This will appropriately convert all alphabetic characters to their flip case counterparts, while non-alphabetic characters like punctuation will remain unchanged.