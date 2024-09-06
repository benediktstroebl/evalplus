```python
def int_to_mini_roman(n):
    if n == 1:
        return "i"
    else:
        hundreds, roman = "", ""
        while n > 0:
            notch = n % 10
            roman = str(notch) + roman
            n //= 10
            if n == 0:
                hundreds = roman
                break
        return hundreds + roman
```

The algorithm works by converting the integer into a string of its base-10 representations, then concatenating them to form the roman numeral. The loop continues until n is zero. When n is zero, the loop ends, and hundreds are stored in the hundreds variable. Then the hundreds and roman are added together and returned to fulfill the function. 

This algorithm has a time complexity of O(log(n)) due to the fact that each digit is converted into a roman numeral and concatenated to the previous ones, and this process is repeated until n equals 0.