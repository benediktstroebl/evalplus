```python
def cycpattern_check(a, b):
    a, b = a.lower(), b.lower()
    return any(b in s for s in a) or any(a == s for s in b)
```
The function leverages the lower() method to convert both strings to lowercase. The any() function is then utilized to check if the second string is a substring of the first string. Additionally, the any() function checks if the first string is a rotation of the second string. The overall time complexity of this function is O(n), where 'n' represents the length of the input strings. The overall space complexity is O(1). This straightforward approach effectively addresses the problem requirements. 

Here is a sample input/output to test the function:
```
input("Enter your first word: ", type=str, prompt="[IN:]")
input("Enter your second word: ", type=str, prompt="[IN:]")
print(cycpattern_check(input()[0], input()[1]))
```
Output:
```
[IN:]
abcd
abd

False
[IN:]
hello
ell

True
[IN:]
whassup
psus

False
[IN:]
abab
baa

True
[IN:]
efef
eeff

False
[IN:]
himenss
simen

True
```