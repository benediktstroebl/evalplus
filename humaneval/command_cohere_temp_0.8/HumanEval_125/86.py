```python
def split_words(txt):
    ans = txt.split(',') if ',' in txt else txt.split() if ' ' in txt else len(txt) if txt.isalpha() else 0
    return ans
```

The problem requires splitting a string of words into a list of words split on whitespace, and, if no whitespace exists in the text, to split on commas. If commas and whitespace do not exist in the text, the function is instructed to return the number of lowercase letters with an odd order in the alphabet. The provided solution uses Python's string splitting methods, str.split() and str.split(',') to split the string on whitespace or commas, respectively. It also uses the built-in function len to calculate the number of lowercase letters in the string, and boolean evaluation txt.isalpha() to determine if the string contains only lowercase letters. 

To better understand the solution, let's break down the code:
- The function split_words takes a string txt as input.
- It first checks if the string contains a comma ('$,'). If it does, it uses the split() method to split the string into a list of words, considering the comma as the separator.
- If the string does not contain a comma, it checks if it contains any whitespace characters (' '). If it does, it again uses the split() method to split the string into a list of words, considering the whitespace as the separator.
- If the string does not contain either commas or whitespace, it further checks if it contains any lowercase letters. If it does, it calculates the length of the string and returns it as the output.
- If none of the above conditions are met, the function returns 0. 

The solution provided assumes the string contains only lowercase letters, and ignores any potential uppercase letters or other non-alphabetic characters that might be present in the input. 

Note that the problem statement does not define the behaviour of the function when the input string is empty, nor does the provided solution. If this is a consideration, you may want to add a special case for empty strings or strings that do not contain any of the specified characters. 

The provided solution is concise and efficient, but it is important to verify that it meets all the edge cases and requirements of the problem as stated in the markdown code block.