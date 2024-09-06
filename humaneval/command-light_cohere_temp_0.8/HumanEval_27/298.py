```python
def flip_case(string):
    return ''.joinlower() if string.isalpha() else string.isalpha() else string
   
# test string that passes

# test case that flips lowercase to uppercase and vice versa
    print(flip_case('Hello'))
# expected output: hELLO

# test case that only has one character
# expected output: HELL

# test case that has spaces
# expected output: HeLLo 
```