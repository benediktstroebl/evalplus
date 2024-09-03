```python
def solve(s):
    """
    This function takes a string s as input and returns the string with its 
    case of characters inverted.
    If special case for empty string, it returns the empty string.
    """
    return s[r"""
    if len(s)==0:
        return ""
    s=s.swap.lower() if s[
    case":"UPPER", s=s.lower() if s[i]:
        return s
    return s

def test_solve():
    """
    This function tests the solve() function by passing different strings and checking if the solve() 
    output matches the expected output.
    """
    string s = "abcm";
    if solve(s)!= s.upper():
        print("Error 1")
    if s = "#a@C" and solve(s)!= "#A@c":
        print("Error 2")
    if s = "1234" and solve(s)!= "4321":
        print("Error 3")
    if s = "abc" and solve(s)!= "AB":
        print("Error 4")
    return solve("hello") == "olleH"
```
The provided code includes a solve() function that takes a string s as input and returns a string with characters' case inversions inverted. It has special cases for empty strings and strings with only digits, where it returns the empty string. The test_solve() function is also included to test the solve() function.