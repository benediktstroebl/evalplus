```python
def correct_bracketing(brackets):
    """ checks if string of brackets has all pairs correctly matched. """

   
    print("Function Signature:", brackets)
    return all(b != ')' for b in brackets)

# Test cases
print(correct_bracketing("()" )) # Expected: True
print(correct_bracketing("("))   # Expected: True
print(correct_bracketing("(()())")) # Expected: True
print(correct_bracketing(")(())"))  # Expected: False
print(correct_bracketing("))("))  # Expected: False
print(correct_bracketing("(((()))))))) # Expected: True
```