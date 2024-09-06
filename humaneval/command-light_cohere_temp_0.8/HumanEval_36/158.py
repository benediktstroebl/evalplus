```python
def fizz_buzz(n):
    count_seven = 0
    for num in range(1, n+1):
        num = str(num)
        divisible_by_11 = any(char == '7' for char in num)
        divisible_by_13 = any(char == '8' for char in num)
        if (divisible_by_11 or divisible_by_13) and num != 7:
            count_seven += 1
    return count_seven
``` 
This code defines a function fizz_buzz that counts the number of occurrences of the number 7 (or 8) in numbers less than n, in such a way that's divisible by 11 or 13. The function iterates through numbers from 1 to n, converts each number to a string, and then uses the any() function to check if any character in the number is 7 or 8. The any_of_7 function is used to check if the number is divisible by 7, and the any_of_8 function is used to check if the number is divisible by 8. The function returns the result in the count of the number 7 (or 8) in the specified range.