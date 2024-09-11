```javascript
// JavaScript solution
function digitSum(s) {
    """Task
    Write a function that takes a string as input and returns the sum of the upper characters only'
    ASCII codes.

    Examples:
        digitSum("") => 0
        digitSum("abAB") => 131
        digitSum("abcCd") => 67
        digitSum("helloE") => 69
        digitSum("woArBld") => 131
        digitSum("aAaaaXa") => 153
    """
    let sum = 0;
    for (let char of s) {
        if (char === char.toUpperCase()) {
            sum += char.charCodeAt(0);
        }
    }
    return sum;
}

console.log(digitSum("")); // 0
console.log(digitSum("abAB")); // 131
console.log(digitSum("abcCd")); // 67
console.log(digitSum("helloE")); // 69
console.log(digitSum("woArBld")); // 131
console.log(digitSum("aAaaaXa")); // 153
```

```python
# Python solution
def digitSum(s):
    """Task
    Write a function that takes a string as input and returns the sum of the upper characters only'
    ASCII codes.

    Examples:
        digitSum("") => 0
        digitSum("abAB") => 131
        digitSum("abcCd") => 67
        digitSum("helloE") => 69
        digitSum("woArBld") => 131
        digitSum("aAaaaXa") => 153
    """
    return sum(ord(char) for char in s if char.isupper())

print(digitSum("")) # 0
print(digitSum("abAB")) # 131
print(digitSum("abcCd")) # 67
print(digitSum("helloE")) # 69
print(digitSum("woArBld")) # 131
print(digitSum("aAaaaXa")) # 153
```

In both the JavaScript and Python solutions, we use a for loop to iterate over each character in the string. If the character is uppercase (i.e., it's equal to its uppercase version), we add its ASCII code to the sum. Finally, we return the sum. The Python solution also uses the `ord` function to get the ASCII code of each character and the `isupper` method to check if a character is uppercase.