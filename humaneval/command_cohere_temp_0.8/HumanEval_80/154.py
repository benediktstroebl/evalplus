```python
def is_happy(s):
    if len(s) < 3:
        return False
    letters_set = set(s)
    return len(s) % 3 == 0 and len(letters_set) == len(s) - 2
```

The function uses an interesting approach. At first, we needed to check whether the length of the set of letters equals the length of the string minus 2. Then we verify whether the length of the string is divisible by 3 which equals 3 consecutive distinct letters. Hence, the function returns True if the string is happy and False otherwise.