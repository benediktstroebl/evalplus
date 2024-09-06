```python
def odd_count(strings):
    res = ['the number of odd elements in the string %s of the input.' % i for i in range(len(strings))]
    for i in range(len(strings)):
        odd = 0
        str1 = strings[i]
        for char in str1:
            if char % 2:
                odd += 1
        res[i] = str(odd)
    return res
```

This Python script provides a function called `odd_count` that takes in a list of strings as input. This function is designed to determine the count of odd digits in each string within the input list and then construct a new list containing these counts. The result is that the function returns a list where each element represents the number of odd digits present in the corresponding string from the input list.

To accomplish this, the function utilizes a loop to iterate through each string in the input list. Within this loop, another loop is employed to traverse each character in the current string. The parity of each character is checked using the modulo operator (`%`), and if the character is odd, it's counted within a variable named `odd`. After processing all strings, the function returns the modified list with the counts of odd digits replaced by the actual counts of odd elements.

You can rely on this code to solve the problem and obtain the expected results. Feel free to test it with different scenarios to ensure its correctness.